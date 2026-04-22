"""SQLite Conversation Store - Agent-First Example"""
from praisonaiagents import Agent, MemoryConfig

# Agent-first approach: use memory with SQLite backend
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    memory=MemoryConfig(
        backend="sqlite",
        session_id="sqlite-session"
    )
)

# Chat - messages are automatically persisted
response = agent.chat("Hello SQLite!")
print(f"Response: {response}")

print("PASSED: SQLite with Agent")
