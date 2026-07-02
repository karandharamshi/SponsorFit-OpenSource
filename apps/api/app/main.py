from fastapi import FastAPI
from pydantic import BaseModel

from packages.sponsorship_detector.classifier import classify_sponsorship

app = FastAPI(title="SponsorFit API")


class SponsorshipRequest(BaseModel):
    text: str


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
