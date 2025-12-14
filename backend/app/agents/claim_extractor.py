import re
from typing import List


class ClaimExtractionAgent:
    """
    Extracts factual claims from raw text.
    """

    def extract_claims(self, text: str) -> List[str]:
        if not text or len(text.strip()) == 0:
            return []

        # Split into sentences
        sentences = re.split(r'[.!?]', text)

        claims = []

        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            # Split compound sentences using conjunctions
            sub_claims = re.split(r'\band\b|\bor\b|\bbut\b', sentence, flags=re.IGNORECASE)

            for claim in sub_claims:
                cleaned = claim.strip()
                if len(cleaned.split()) >= 3:
                    claims.append(cleaned)

        return claims
