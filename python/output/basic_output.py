#!/usr/bin/env python3
"""
Basic Output Example for PraisonAI Agents.

This example demonstrates how to control agent output via instructions.

Usage:
    python basic_output.py
"""

from praisonaiagents import Agent

# Agent-centric quickstart: Create agents with different output styles via instructions
concise_agent = Agent(
    name="ConciseBot",
    instructions="You are a helpful assistant. Be extremely concise - respond in 1-2 sentences max."
)

detailed_agent = Agent(
    name="DetailedBot", 
    instructions="You are a helpful assistant. Provide detailed, comprehensive responses with examples."
)


def main():
    print("=" * 60)
    print("Agent-Centric Output Demo")
    print("=" * 60)
    
    print(f"\nConcise Agent: {concise_agent.name}")
    print(f"Detailed Agent: {detailed_agent.name}")
    
    print("\n--- Testing Concise Agent ---")
    result = concise_agent.chat("What is Python?")
    print(f"Response: {result}")
    
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
