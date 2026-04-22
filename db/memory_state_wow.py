"""Memory State Store - Agent-First Example"""
from praisonaiagents import Agent

# Agent-first approach: in-memory state (no persistence)
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    memory={"session_id": "memory-session"}
)

# Chat - messages stored in memory only
response = agent.chat("Hello Memory!")
print(f"Response: {response}")

print("PASSED: Memory with Agent")

# --- Advanced: Direct Store Usage ---
# from praisonai.persistence import create_state_store
# store = create_state_store("memory")
