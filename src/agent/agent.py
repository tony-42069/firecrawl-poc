# src/agent/agent.py
from anthropic import Anthropic
import os
from dotenv import load_dotenv

class FirecrawlAgent:
    def __init__(self):
        load_dotenv()
        self.anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = "claude-3-opus-20240229"

    async def research_trending_tech(self, category="web-development"):
        """Research trending technologies in a specific category."""
        prompt = f"""Research the latest trending technologies in {category}. 
        Focus on tools and frameworks that could be integrated with Firecrawl.
        Format the response as a structured list of technologies with their key features and potential use cases."""
        
        message = self.anthropic.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        return message.content[0].text

    async def generate_example_app(self, tech_stack, use_case):
        """Generate an example application using specified technology stack."""
        prompt = f"""Create a complete example application that demonstrates Firecrawl integration with {tech_stack}.
        Use case: {use_case}
        Include:
        - Full application code
        - Setup instructions
        - Integration details
        - Best practices
        Format as a structured markdown document."""
        
        message = self.anthropic.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        return message.content[0].text