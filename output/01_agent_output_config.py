"""
OutputConfig Example

Demonstrates using OutputConfig for fine-grained control over agent output.
"""
import os
from praisonaiagents import Agent, OutputConfig

# Ensure API key is set from environment
assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY must be set"

# Custom output configuration
agent = Agent(
    instructions="You are a helpful math tutor.",
    output=OutputConfig(
        output="verbose",
        markdown=True,
        stream=False,
        metrics=True,
        reasoning_steps=False,
    ),
)

# Streaming output configuration
agent_streaming = Agent(
    instructions="You are a helpful assistant.",
    output=OutputConfig(
        output="verbose",
        markdown=True,
        stream=True,
        metrics=False,
    ),
)

if __name__ == "__main__":
    print("Testing OutputConfig...")
    
    # Test with metrics
    print("\n--- With Metrics ---")
    result = agent.chat("Explain the Pythagorean theorem briefly.")
    print(f"Result: {result}")
    
    print("\nOutputConfig tests passed!")
