"""PostgreSQL Conversation Store - Agent-First Example (requires Docker)

Docker: docker run -d --name pg -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:15
"""
import os
from praisonaiagents import Agent, db

# Agent-first approach: use memory parameter
url = os.getenv("POSTGRES_URL", "postgresql://postgres:postgres@localhost:5432/postgres")

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    memory={"backend": "postgres", "session_id": "pg-session", "config": {"url": url}}
)

# Chat - messages are automatically persisted
response = agent.chat("Hello Postgres!")
print(f"Response: {response}")

# Verify persistence
print("PASSED: PostgreSQL with Agent")

# --- Advanced: Direct Store Usage ---
# For direct store access without an agent:
# from praisonai.persistence import create_conversation_store
# store = create_conversation_store("postgres", url=url)
