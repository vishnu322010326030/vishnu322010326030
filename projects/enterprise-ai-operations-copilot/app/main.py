from time import perf_counter

from fastapi import FastAPI

from app.models import HealthResponse, QueryRequest, QueryResponse
from app.services.retrieval import answer_business_question

app = FastAPI(
    title="Enterprise AI Operations Copilot",
    version="0.1.0",
    description="Production-style starter API for grounded business operations Q&A.",
)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="enterprise-ai-operations-copilot")


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest) -> QueryResponse:
    started = perf_counter()
    answer, sources = answer_business_question(request.question)
    latency_ms = round((perf_counter() - started) * 1000, 2)

    return QueryResponse(
        question=request.question,
        answer=answer,
        sources=sources,
        latency_ms=latency_ms,
    )
