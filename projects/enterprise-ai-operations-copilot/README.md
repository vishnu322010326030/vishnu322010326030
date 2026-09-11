# Enterprise AI Operations Copilot

A production-style AI operations assistant designed to help business users ask questions across structured operational data and internal documents.

## Why this project

The project demonstrates an end-to-end AI engineering workflow: business requirements, API design, structured and unstructured retrieval, caching, testing, containerization, observability, and performance benchmarking.

## Core capabilities

- FastAPI backend with health and query endpoints
- Hybrid retrieval pattern for structured data and document context
- PostgreSQL-ready persistence layer
- Redis-ready response caching
- Retrieval-Augmented Generation architecture
- Docker-based local deployment
- Automated API tests
- Latency measurement hooks for performance benchmarking
- Client feedback field for iterative product improvement

## Architecture

Client -> FastAPI -> Cache -> Retrieval Layer -> Structured Data / Documents -> Response

The current repository is a working starter implementation. Cloud deployment, load testing, and production observability are intentionally tracked as implementation milestones rather than claimed as completed work.

## Project structure

```text
enterprise-ai-operations-copilot/
|-- app/
|   |-- main.py
|   |-- models.py
|   `-- services/
|       `-- retrieval.py
|-- tests/
|   `-- test_api.py
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
`-- .env.example
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://localhost:8000/docs` for the Swagger UI.

## Docker

```bash
docker compose up --build
```

## Example request

```json
POST /query
{
  "question": "Which operational area has the highest number of unresolved issues?",
  "user_id": "demo-user"
}
```

## Planned engineering milestones

1. Connect PostgreSQL operational tables
2. Add document ingestion and vector retrieval
3. Add Redis caching and cache-hit metrics
4. Add LLM provider abstraction and grounded response generation
5. Add Locust load tests for latency and throughput benchmarking
6. Add AWS deployment configuration
7. Add structured logging and monitoring dashboards
8. Add a lightweight client-facing UI and feedback loop

## Resume-safe status

Implemented now: FastAPI service structure, request validation, retrieval abstraction, health/query endpoints, automated API tests, Docker configuration, and latency tracking.

Do not claim AWS deployment, production scale, Redis performance gains, or benchmark improvements until those milestones are actually implemented and measured.
