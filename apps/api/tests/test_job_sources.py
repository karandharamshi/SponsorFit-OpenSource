from pathlib import Path

from packages.job_sources import import_jobs_from_csv
from packages.sponsorship_detector.classifier import SponsorshipStatus


def test_import_jobs_from_example_csv():
    jobs = import_jobs_from_csv(Path("examples/jobs.example.csv"))

    assert len(jobs) == 2
    assert jobs[0].title == "Software Developer"
    assert jobs[0].salary_gbp == 45000
    assert jobs[0].skills == ["apis", "python", "sql"]
    assert jobs[0].sponsorship.status == SponsorshipStatus.CLEAR
    assert jobs[1].sponsorship.status == SponsorshipStatus.NOT_AVAILABLE
