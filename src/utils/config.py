import os
from dotenv import load_dotenv
from typing import Dict

def load_config() -> Dict[str, str]:
    """
    Load configuration from environment variables.
    Returns a dictionary containing all necessary configuration parameters.
    """
    load_dotenv()
    
    required_vars = ["ANTHROPIC_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )
    
    return {
        "anthropic_api_key": os.getenv("ANTHROPIC_API_KEY"),
        "model": "claude-3-opus-20240229",
        "max_examples": 3,  # Maximum number of examples to generate per batch
        "github_repo": "firecrawl/examples",
        "base_prompts_dir": os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "prompts"
        ),
    }

def get_config(key: str) -> str:
    """
    Get a specific configuration value.
    Args:
        key: The configuration key to retrieve
    Returns:
        The value for the specified key
    Raises:
        KeyError: If the key doesn't exist in the configuration
    """
    config = load_config()
    if key not in config:
        raise KeyError(f"Configuration key '{key}' not found")
    return config[key]