from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from packages.sponsorship_detector.classifier import SponsorshipResult, classify_sponsorship

KNOWN_SKILLS = {
    "python",
    "sql",
    "apis",
    "api",
    "fastapi",
    "django",
    "flask",
    "javascript",
    "typescript",
    "react",
    "aws",
    "azure",
    "docker",
    "kubernetes",
    "support",
}


@dataclass(frozen=True)
class ImportedJob:
    title: str
    company: str
    salary_gbp: int | None
    location: str
    url: str
    description: str
    skills: list[str]
    sponsorship: SponsorshipResult


def import_jobs_from_csv(path: str | Path) -> list[ImportedJob]:
    """Import jobs from a CSV file using the repo example schema."""
    rows: list[ImportedJob] = []
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            description = (row.get("description") or "").strip()
            rows.append(
                ImportedJob(
                    title=(row.get("title") or "").strip(),
                    company=(row.get("company") or "").strip(),
                    salary_gbp=_parse_salary(row.get("salary")),
                    location=(row.get("location") or "").strip(),
                    url=(row.get("url") or "").strip(),
                    description=description,
                    skills=_extract_skills(description),
                    sponsorship=classify_sponsorship(description),
                )
            )
    return rows


def _parse_salary(value: str | None) -> int | None:
    if value is None:
        return None
    digits = "".join(char for char in value if char.isdigit())
    return int(digits) if digits else None


def _extract_skills(description: str) -> list[str]:
    words = {word.strip(".,()").lower() for word in description.split()}
    return sorted(skill for skill in KNOWN_SKILLS if skill in words)
