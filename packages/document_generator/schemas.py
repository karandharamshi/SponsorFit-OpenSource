from __future__ import annotations

from pydantic import BaseModel


class ApplicationAnswer(BaseModel):
    question: str
    answer: str
    requires_human_review: bool


class SensitiveQuestion(BaseModel):
    question: str
    reason: str


class DraftApplicationPack(BaseModel):
    cv_summary: str
    skills_section: list[str]
    experience_bullets: list[str]
    cover_letter: str
    application_answers: list[ApplicationAnswer]
    sensitive_questions: list[SensitiveQuestion]
