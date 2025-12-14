# from typing import Dict


# class FactVerificationAgent:
#     """
#     Verifies factual claims against known trusted information.
#     """

#     def verify_claim(self, claim: str) -> Dict:
#         claim_lower = claim.lower()

#         # Simple rule-based knowledge (baseline)
#         if "vaccines cause infertility" in claim_lower:
#             return {
#                 "claim": claim,
#                 "verdict": "FALSE",
#                 "explanation": "Extensive scientific studies show vaccines do not cause infertility."
#             }

#         if "who is lying" in claim_lower:
#             return {
#                 "claim": claim,
#                 "verdict": "MISLEADING",
#                 "explanation": "This is a broad accusation without specific evidence."
#             }

#         # Default fallback
#         return {
#             "claim": claim,
#             "verdict": "UNKNOWN",
#             "explanation": "Insufficient data to verify this claim."
#         }
from app.services.retriever import RetrieverService
from backend.app.services.llm.groq_llm import GeminiLLMService


class FactVerificationAgent:
    def __init__(self):
        self.retriever = RetrieverService()
        self.llm = GeminiLLMService()

    def verify_claim(self, claim: str):
        context = self.retriever.retrieve(claim)

        if not context:
            return {
                "claim": claim,
                "verdict": "UNKNOWN",
                "explanation": "No trusted information found."
            }

        ai_response = self.llm.verify_claim(claim, context)

        return {
            "claim": claim,
            "ai_response": ai_response
        }
