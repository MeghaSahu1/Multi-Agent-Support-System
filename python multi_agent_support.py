# multi_agent_support.py

class IntentAgent:
    """
    Identifies the user's intent from a query.
    """
    def __init__(self):
        self.intents = {
            "billing": ["bill", "invoice", "payment"],
            "technical": ["error", "issue", "bug", "problem"],
            "general": ["hello", "hi", "info", "question"]
        }

    def classify_intent(self, query: str) -> str:
        query_lower = query.lower()
        for intent, keywords in self.intents.items():
            if any(keyword in query_lower for keyword in keywords):
                return intent
        return "general"


class ReplyAgent:
    """
    Generates responses based on intent.
    """
    responses = {
        "billing": "Our billing team will contact you shortly regarding your invoice.",
        "technical": "Please describe the issue in detail so we can assist you technically.",
        "general": "Hello! How can I help you today?"
    }

    def generate_reply(self, intent: str) -> str:
        return self.responses.get(intent, "I'm not sure how to respond to that. Can you clarify?")


class EscalationAgent:
    """
    Determines if a query needs escalation.
    """
    def __init__(self):
        self.escalation_keywords = ["urgent", "not working", "fail", "critical"]

    def needs_escalation(self, query: str) -> bool:
        query_lower = query.lower()
        return any(keyword in query_lower for keyword in self.escalation_keywords)


class Orchestrator:
    """
    Coordinates multiple agents for customer support.
    """
    def __init__(self):
        self.intent_agent = IntentAgent()
        self.reply_agent = ReplyAgent()
        self.escalation_agent = EscalationAgent()

    def handle_query(self, query: str) -> dict:
        intent = self.intent_agent.classify_intent(query)
        response = self.reply_agent.generate_reply(intent)
        escalation = self.escalation_agent.needs_escalation(query)
        return {
            "query": query,
            "intent": intent,
            "response": response,
            "escalation_required": escalation
        }


def main():
    orchestrator = Orchestrator()
    print("=== Multi-Agent Customer Support ===")
    
    while True:
        user_query = input("\nEnter customer query (or 'exit' to quit): ")
        if user_query.lower() == "exit":
            print("Exiting system. Goodbye!")
            break

        result = orchestrator.handle_query(user_query)
        print("\n--- Response ---")
        print(f"Intent: {result['intent']}")
        print(f"Response: {result['response']}")
        print(f"Escalation Required: {result['escalation_required']}")


if __name__ == "__main__":
    main()
