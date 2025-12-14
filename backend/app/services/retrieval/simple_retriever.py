from app.data.knowledge_base import KNOWLEDGE_BASE


class SimpleRetriever:
    def retrieve(self, claim: str) -> str:
        """
        Naive keyword-based retrieval from trusted knowledge base.
        """
        matched = []

        for item in KNOWLEDGE_BASE:
            if any(word.lower() in item["content"].lower() for word in claim.split()):
                matched.append(f"- ({item['source']}) {item['content']}")

        if not matched:
            return "No relevant trusted information found."

        return "\n".join(matched)
