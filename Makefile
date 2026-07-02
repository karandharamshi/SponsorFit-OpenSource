.PHONY: test lint format run-api

test:
	python -m pytest

lint:
	python -m ruff check .

format:
	python -m ruff format .

run-api:
	python -m uvicorn apps.api.app.main:app --reload
