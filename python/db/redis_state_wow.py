"""Redis State Store - Agent-First Example (requires Docker)

Docker: docker run -d --name redis -p 6379:6379 redis:7
"""
import os
from praisonaiagents import Agent, db

url = os.getenv("REDIS_URL", "redis://localhost:6379")

# Agent-first approach: use memory parameter with Redis state store
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    memory={"backend": "redis", "session_id": "redis-session", "config": {
        "db_url": "sqlite:///conversations.db",
        "state_url": url,
    }}
)

# Chat - messages persisted with Redis state
response = agent.chat("Hello Redis!")
print(f"Response: {response}")

print("PASSED: Redis with Agent")

# --- Advanced: Direct Store Usage ---
# from praisonai.persistence import create_state_store
# store = create_state_store("redis", url=url)
