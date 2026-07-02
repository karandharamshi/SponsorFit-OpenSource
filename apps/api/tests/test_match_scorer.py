from packages.match_scorer.scorer import JobInput, UserProfile, score_job
from packages.sponsorship_detector.classifier import SponsorshipStatus


def test_rejects_no_sponsorship():
    job = JobInput(
        title="Software Developer",
        salary_gbp=50000,
        location="London",
        skills=["Python"],
        sponsorship_status=SponsorshipStatus.NOT_AVAILABLE,
    )
    user = UserProfile(minimum_salary_gbp=41700, locations=["London"], skills=["Python"])
    assert score_job(job, user).score == 0


def test_salary_below_threshold_is_flagged():
    job = JobInput(
        title="Software Developer",
        salary_gbp=40000,
        location="London",
        skills=["Python"],
        sponsorship_status=SponsorshipStatus.CLEAR,
    )
    user = UserProfile(minimum_salary_gbp=41700, locations=["London"], skills=["Python"])

    result = score_job(job, user)

    assert "Salary is missing or below threshold." in result.reasons
    assert result.score == 5.8


def test_skills_matching_increases_score():
    job = JobInput(
        title="Backend Engineer",
        salary_gbp=50000,
        location="Remote UK",
        skills=["Python", "SQL", "Docker"],
        sponsorship_status=SponsorshipStatus.LIKELY,
    )
    user = UserProfile(minimum_salary_gbp=41700, locations=["Remote"], skills=["Python", "SQL", "FastAPI"])

    result = score_job(job, user)

    assert "Matched 2 skills." in result.reasons
    assert result.score == 7.5
