from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.claim_extractor import ClaimExtractionAgent

router = APIRouter()
agent = ClaimExtractionAgent()


class IngestRequest(BaseModel):
    text: str


@router.post("/ingest")
def ingest_text(request: IngestRequest):
    claims = agent.extract_claims(request.text)

    return {
        "original_text": request.text,
        "extracted_claims": claims
    }
