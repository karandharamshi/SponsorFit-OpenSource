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
