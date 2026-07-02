from packages.sponsorship_detector.classifier import SponsorshipStatus, classify_sponsorship


def test_clear_sponsorship():
    result = classify_sponsorship("We can provide Skilled Worker sponsorship for this role.")
    assert result.status == SponsorshipStatus.CLEAR


def test_not_available():
    result = classify_sponsorship("Sponsorship is not available for this vacancy.")
    assert result.status == SponsorshipStatus.NOT_AVAILABLE


def test_unknown():
    result = classify_sponsorship("We are hiring a Python developer.")
    assert result.status == SponsorshipStatus.UNKNOWN


def test_uk_skilled_worker_phrase_is_clear():
    result = classify_sponsorship(
        "UK Skilled Worker sponsorship is available and a certificate of sponsorship will be provided."
    )
    assert result.status == SponsorshipStatus.CLEAR
    assert "uk skilled worker sponsorship" in result.evidence


def test_right_to_work_phrase_rejects_even_with_sponsorship_wording():
    result = classify_sponsorship(
        "Applicants must already have the right to work in the UK and no sponsorship available."
    )
    assert result.status == SponsorshipStatus.NOT_AVAILABLE
