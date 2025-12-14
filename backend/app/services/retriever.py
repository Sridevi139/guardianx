from app.data.trusted_facts import TRUSTED_FACTS


class RetrieverService:
    """
    Retrieves relevant trusted context for a claim.
    """

    def retrieve(self, claim: str) -> str:
        claim_lower = claim.lower()
        contexts = []

        for fact in TRUSTED_FACTS:
            if fact["topic"] in claim_lower:
                contexts.append(fact["content"])

        return " ".join(contexts)
