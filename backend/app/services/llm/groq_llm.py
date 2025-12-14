import os
import json
from groq import Groq


class GroqLLMService:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment")

        self.client = Groq(api_key=api_key)

    def verify_claim(self, claim: str, context: str = "") -> dict:
        """
        Claim verification with concise, relevant factual explanation.
        """

        prompt = f"""
You are a professional fact-checking system.

Claim:
"{claim}"

Instructions:
- Determine whether the claim is TRUE, FALSE, MISLEADING, or UNKNOWN.
- Use general factual knowledge where appropriate.
- Explanation must be directly related to the subject of the claim.
- Do NOT introduce unrelated topics.
- Do NOT mention training data, cutoff dates, or sources unless necessary.
- Keep explanation short (1–2 sentences max).
- Explanation should add useful factual context, not filler.

Respond ONLY in valid JSON:

{{
  "verdict": "TRUE | FALSE | MISLEADING | UNKNOWN",
  "explanation": "Concise explanation directly related to the claim"
}}
"""

        try:
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=200
            )

            content = response.choices[0].message.content.strip()
            return json.loads(content)

        except Exception as e:
            print("❌ Groq error:", e)
            return {
                "verdict": "UNKNOWN",
                "explanation": "Unable to verify the claim at this time."
            }
