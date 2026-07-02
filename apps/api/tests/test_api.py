from fastapi.testclient import TestClient

from apps.api.app.main import app

client = TestClient(app)


def test_score_endpoint_with_direct_job():
    response = client.post(
        "/jobs/score",
        json={
            "job": {
                "title": "Platform Engineer",
                "salary_gbp": 50000,
                "location": "London",
                "skills": ["Python", "SQL"],
                "description": "Visa sponsorship available for this Skilled Worker role.",
            },
            "user": {
                "minimum_salary_gbp": 41700,
                "locations": ["London"],
                "skills": ["Python", "FastAPI"],
            },
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["sponsorship"]["status"] == "clear"
    assert body["score"] == 7.8
    assert "Salary meets threshold." in body["reasons"]


def test_score_endpoint_with_csv_import():
    response = client.post(
        "/jobs/score",
        json={
            "job": {
                "csv_path": "examples/jobs.example.csv",
                "csv_row_index": 1,
            },
            "user": {
                "minimum_salary_gbp": 41700,
                "locations": ["Birmingham"],
                "skills": ["Support", "Python"],
            },
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["score"] == 0
    assert body["sponsorship"]["status"] == "not_available"
    assert body["reasons"] == ["Rejected because sponsorship is not available."]
