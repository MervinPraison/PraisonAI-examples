"""JSON Conversation Store - Agent-First Example"""
from praisonaiagents import Agent, db

# Agent-first approach: use memory parameter with db instance
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    memory={"backend": "file", "session_id": "json-session"}
)

# Chat - messages are automatically persisted
response = agent.chat("Hello JSON!")
print(f"Response: {response}")

print("PASSED: JSON with Agent")

# --- Advanced: Direct Store Usage ---
# from praisonai.persistence import create_conversation_store
# store = create_conversation_store("json", path="/tmp/json_demo")
