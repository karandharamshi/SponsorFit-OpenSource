from __future__ import annotations

from dataclasses import dataclass

from packages.sponsorship_detector.classifier import SponsorshipStatus


@dataclass(frozen=True)
class JobInput:
    title: str
    salary_gbp: int | None
    location: str
    skills: list[str]
    sponsorship_status: SponsorshipStatus


@dataclass(frozen=True)
class UserProfile:
    minimum_salary_gbp: int
    locations: list[str]
    skills: list[str]


@dataclass(frozen=True)
class ScoreResult:
    score: float
    reasons: list[str]


def score_job(job: JobInput, user: UserProfile) -> ScoreResult:
    """Score a job from 0 to 10 with simple transparent rules."""
    score = 0.0
    reasons: list[str] = []

    if job.sponsorship_status == SponsorshipStatus.NOT_AVAILABLE:
        return ScoreResult(0.0, ["Rejected because sponsorship is not available."])

    if job.sponsorship_status == SponsorshipStatus.CLEAR:
        score += 3
        reasons.append("Clear sponsorship evidence.")
    elif job.sponsorship_status == SponsorshipStatus.LIKELY:
        score += 2
        reasons.append("Likely sponsorship evidence.")
    else:
        score += 0.5
        reasons.append("Sponsorship is unknown.")

    if job.salary_gbp is not None and job.salary_gbp >= user.minimum_salary_gbp:
        score += 2
        reasons.append("Salary meets threshold.")
    else:
        reasons.append("Salary is missing or below threshold.")

    matched_skills = {s.lower() for s in job.skills} & {s.lower() for s in user.skills}
    skill_score = min(3, len(matched_skills) * 0.75)
    score += skill_score
    reasons.append(f"Matched {len(matched_skills)} skills.")

    if any(loc.lower() in job.location.lower() for loc in user.locations):
        score += 1.5
        reasons.append("Location matches preference.")
    else:
        reasons.append("Location does not clearly match preference.")

    if any(level in job.title.lower() for level in ["junior", "associate", "developer", "support", "analyst", "engineer"]):
        score += 0.5
        reasons.append("Title appears relevant.")

    return ScoreResult(round(min(score, 10.0), 1), reasons)
