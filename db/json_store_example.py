"""
JSON ConversationStore - Agent-First Example

Demonstrates using the JSON file-based conversation store with an Agent.
No external dependencies required.
"""

from praisonaiagents import Agent, MemoryConfig


def main():
    print("=== JSON Conversation Store (Agent-First) ===")
    
    # Agent-first approach: use memory with file backend (JSON-based)
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        memory=MemoryConfig(
            backend="file",
            session_id="json-example-session"
        )
    )
    
    # Chat - messages are automatically persisted to JSON files
    response = agent.chat("Hello! What's the weather like in San Francisco?")
    print(f"Response: {response}")
    
    # Second message to test conversation continuity
    response2 = agent.chat("What about New York?")
    print(f"Response: {response2}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
