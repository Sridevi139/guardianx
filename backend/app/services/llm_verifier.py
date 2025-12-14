import os
from together import Together


class LLMVerifierService:
    """
    Uses Together AI LLM to verify claims using retrieved context.
    """

    def __init__(self):
        self.client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

    def verify(self, claim: str, context: str) -> dict:
        prompt = f"""
You are a fact-checking AI.

Claim:
"{claim}"

Trusted Context:
"{context}"

Based ONLY on the trusted context, classify the claim as:
- TRUE
- FALSE
- MISLEADING
- UNKNOWN

Then explain why.

Respond in JSON with keys: verdict, explanation.
"""

        response = self.client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return response.choices[0].message.content
