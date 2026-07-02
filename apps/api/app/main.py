from __future__ import annotations

from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from packages.job_sources import import_jobs_from_csv
from packages.match_scorer.scorer import JobInput, UserProfile, score_job
from packages.sponsorship_detector.classifier import SponsorshipResult, classify_sponsorship

app = FastAPI(title="SponsorFit API")


class SponsorshipRequest(BaseModel):
    text: str


class ScoreJobRequest(BaseModel):
    title: Optional[str] = None
    salary_gbp: Optional[int] = None
    location: Optional[str] = None
    skills: list[str] = Field(default_factory=list)
    description: str = ""
    csv_path: Optional[str] = None
    csv_row_index: int = 0


class ScoreUserRequest(BaseModel):
    minimum_salary_gbp: int
    locations: list[str]
    skills: list[str]


class ScoreRequest(BaseModel):
    job: ScoreJobRequest
    user: ScoreUserRequest


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/jobs/classify-sponsorship")
def classify(request: SponsorshipRequest):
    result = classify_sponsorship(request.text)
    return {
        "status": result.status.value,
        "evidence": result.evidence,
        "reason": result.reason,
    }


@app.post("/jobs/score")
def score(request: ScoreRequest):
    job, sponsorship = _build_job_input(request.job)
    result = score_job(
        job,
        UserProfile(
            minimum_salary_gbp=request.user.minimum_salary_gbp,
            locations=request.user.locations,
            skills=request.user.skills,
        ),
    )
    return {
        "score": result.score,
        "reasons": result.reasons,
        "sponsorship": {
            "status": sponsorship.status.value,
            "evidence": sponsorship.evidence,
            "reason": sponsorship.reason,
        },
    }


def _build_job_input(request: ScoreJobRequest) -> tuple[JobInput, SponsorshipResult]:
    if request.csv_path:
        imported_jobs = import_jobs_from_csv(_resolve_csv_path(request.csv_path))
        try:
            imported_job = imported_jobs[request.csv_row_index]
        except IndexError as exc:
            raise HTTPException(status_code=400, detail="CSV row index out of range.") from exc
        return (
            JobInput(
                title=imported_job.title,
                salary_gbp=imported_job.salary_gbp,
                location=imported_job.location,
                skills=imported_job.skills,
                sponsorship_status=imported_job.sponsorship.status,
            ),
            imported_job.sponsorship,
        )

    if not request.title or not request.location:
        raise HTTPException(status_code=400, detail="Direct job scoring requires title and location.")

    sponsorship = classify_sponsorship(request.description)
    return (
        JobInput(
            title=request.title,
            salary_gbp=request.salary_gbp,
            location=request.location,
            skills=request.skills,
            sponsorship_status=sponsorship.status,
        ),
        sponsorship,
    )


def _resolve_csv_path(csv_path: str) -> Path:
    path = Path(csv_path)
    return path if path.is_absolute() else Path.cwd() / path
