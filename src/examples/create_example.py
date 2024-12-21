# src/examples/create_example.py
import asyncio
from agent.agent import FirecrawlAgent

async def main():
    agent = FirecrawlAgent()
    
    # Research trending technologies
    trends = await agent.research_trending_tech("web-development")
    print("Trending Technologies:")
    print(trends)
    
    # Generate an example app
    example = await agent.generate_example_app(
        "Next.js + Firecrawl",
        "Building a real-time news aggregator with semantic search"
    )
    print("\nGenerated Example:")
    print(example)

if __name__ == "__main__":
    asyncio.run(main())