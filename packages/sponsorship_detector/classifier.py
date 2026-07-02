from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class SponsorshipStatus(str, Enum):
    CLEAR = "clear"
    LIKELY = "likely"
    UNKNOWN = "unknown"
    NOT_AVAILABLE = "not_available"


@dataclass(frozen=True)
class SponsorshipResult:
    status: SponsorshipStatus
    evidence: list[str]
    reason: str


NEGATIVE_PHRASES = [
    "sponsorship is not available",
    "we cannot offer sponsorship",
    "unable to sponsor",
    "must have the right to work",
    "must already have the right to work",
    "no visa sponsorship",
    "no sponsorship available",
    "this role does not qualify for sponsorship",
    "we are unable to provide visa sponsorship",
]

CLEAR_PHRASES = [
    "skilled worker sponsorship",
    "certificate of sponsorship",
    "visa sponsorship available",
    "sponsorship available",
    "sponsorship can be provided",
    "we can sponsor",
    "uk skilled worker sponsorship",
    "skilled worker visa sponsorship",
    "skilled worker route sponsorship",
    "certificate of sponsorship will be provided",
    "cos provided",
    "switch into the skilled worker route",
]

LIKELY_PHRASES = [
    "sponsorship considered",
    "eligible for sponsorship",
    "licensed sponsor",
    "skilled worker visa",
    "home office sponsor licence",
    "a-rated sponsor",
    "candidate requiring sponsorship",
    "visa sponsorship may be available",
    "skilled worker route",
]


def classify_sponsorship(text: str) -> SponsorshipResult:
    """Classify sponsorship evidence from job text."""
    normalised = text.lower()

    for phrase in NEGATIVE_PHRASES:
        if phrase in normalised:
            return SponsorshipResult(
                status=SponsorshipStatus.NOT_AVAILABLE,
                evidence=[phrase],
                reason="The job text says sponsorship is not available or requires existing right to work.",
            )

    evidence = [phrase for phrase in CLEAR_PHRASES if phrase in normalised]
    if evidence:
        return SponsorshipResult(
            status=SponsorshipStatus.CLEAR,
            evidence=evidence,
            reason="The job text explicitly mentions sponsorship availability.",
        )

    evidence = [phrase for phrase in LIKELY_PHRASES if phrase in normalised]
    if evidence:
        return SponsorshipResult(
            status=SponsorshipStatus.LIKELY,
            evidence=evidence,
            reason="The job text contains sponsorship-related clues but is not fully explicit.",
        )

    return SponsorshipResult(
        status=SponsorshipStatus.UNKNOWN,
        evidence=[],
        reason="No clear sponsorship evidence found.",
    )
