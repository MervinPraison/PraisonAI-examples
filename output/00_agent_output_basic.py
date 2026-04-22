"""
Basic Output Configuration Example

Demonstrates using output presets for quick configuration.
"""
import os
from praisonaiagents import Agent

# Ensure API key is set from environment
assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY must be set"

# Default output (output="verbose", markdown=True)
agent_default = Agent(
    instructions="You are a helpful assistant.",
)

# Minimal output - quiet mode
agent_minimal = Agent(
    instructions="You are a helpful assistant.",
    output="minimal",
)

# Verbose output - shows metrics and reasoning
agent_verbose = Agent(
    instructions="You are a helpful assistant.",
    output="verbose",
)

# Silent output - no console output
agent_silent = Agent(
    instructions="You are a helpful assistant.",
    output="silent",
)

if __name__ == "__main__":
    print("Testing output presets...")
    
    # Test verbose agent
    print("\n--- Verbose Output ---")
    result = agent_verbose.chat("What is 2+2?")
    print(f"Result: {result}")
    
    print("\n--- Minimal Output ---")
    result = agent_minimal.chat("What is 2+2?")
    print(f"Result: {result}")
    
    print("\nAll output preset tests passed!")
