# tests/test_setup.py
import asyncio
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent.agent import FirecrawlAgent
from src.utils.config import load_config

async def test_agent_initialization():
    """Test that the agent can be initialized with config"""
    try:
        agent = FirecrawlAgent()
        assert agent is not None
        print("✅ Agent initialization successful")
    except Exception as e:
        print(f"❌ Agent initialization failed: {str(e)}")
        raise e

async def test_research_capability():
    """Test that the agent can research trending tech"""
    agent = FirecrawlAgent()
    try:
        result = await agent.research_trending_tech("web-development")
        assert result is not None and len(result) > 0
        print("✅ Research capability test successful")
        print("Sample research result:", result[:200] + "...")
    except Exception as e:
        print(f"❌ Research capability test failed: {str(e)}")
        raise e

async def test_example_generation():
    """Test that the agent can generate example apps"""
    agent = FirecrawlAgent()
    try:
        result = await agent.generate_example_app(
            "Next.js",
            "Building a web scraper dashboard"
        )
        assert result is not None and len(result) > 0
        print("✅ Example generation test successful")
        print("Sample example:", result[:200] + "...")
    except Exception as e:
        print(f"❌ Example generation test failed: {str(e)}")
        raise e

async def main():
    """Run all tests"""
    print("\n🔍 Testing Firecrawl Agent Setup...")
    
    try:
        config = load_config()
        print("✅ Configuration loaded successfully")
    except Exception as e:
        print(f"❌ Configuration loading failed: {str(e)}")
        return

    await test_agent_initialization()
    await test_research_capability()
    await test_example_generation()
    
    print("\n✨ All tests completed!")

if __name__ == "__main__":
    asyncio.run(main())