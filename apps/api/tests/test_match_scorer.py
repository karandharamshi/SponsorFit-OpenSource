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
