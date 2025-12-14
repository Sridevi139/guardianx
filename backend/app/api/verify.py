from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List
from app.services.llm.groq_llm import GroqLLMService
import traceback

router = APIRouter(prefix="/verify", tags=["Fact Verification"])
llm = GroqLLMService()


class VerifyRequest(BaseModel):
    claims: List[str]


@router.post("")
def verify_claims(req: VerifyRequest):
    """
    Verify multiple claims (UI / normal API usage)
    """
    results = []

    for claim in req.claims:
        try:
            print(f"🔍 Verifying claim: {claim}")

            result = llm.verify_claim(
                claim=claim,
                context="Vaccines are extensively tested for safety by global health organizations."
            )

            results.append({
                "claim": claim,
                "verdict": result.get("verdict", "UNKNOWN"),
                "explanation": result.get("explanation", "")
            })

        except Exception as e:
            traceback.print_exc()
            results.append({
                "claim": claim,
                "verdict": "ERROR",
                "explanation": str(e)
            })

    return {
        "count": len(results),
        "results": results
    }


@router.post("/kestra")
def verify_claim_kestra(claim: str = Body(..., embed=True)):
    """
    Single-claim endpoint designed for Kestra workflows
    """
    try:
        result = llm.verify_claim(
            claim=claim,
            context="Vaccines are extensively tested for safety by global health organizations."
        )

        return {
            "claim": claim,
            "verdict": result.get("verdict", "UNKNOWN"),
            "explanation": result.get("explanation", "")
        }

    except Exception as e:
        traceback.print_exc()
        return {
            "claim": claim,
            "error": str(e)
        }
