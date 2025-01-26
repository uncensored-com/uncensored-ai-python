import os
import json
from pathlib import Path

_CONFIG_DIR = Path.home() / ".config" / "uncensored"
_CONFIG_FILE = _CONFIG_DIR / "config.json"

def set_api_key(key: str):
    """Set the API key both in memory and in the config file."""
    from . import api_key as global_api_key
    global_api_key = key

    _CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "api_key": key
    }
    with open(_CONFIG_FILE, "w") as f:
        json.dump(data, f)

    os.environ["UNCENSORED_API_KEY"] = key

def get_api_key() -> str:
    """Get the API key from memory, environment, or config file."""
    from . import api_key as global_api_key
    if global_api_key:
        return global_api_key

    env_key = os.getenv("UNCENSORED_API_KEY", None)
    if env_key:
        return env_key

    if _CONFIG_FILE.is_file():
        with open(_CONFIG_FILE, "r") as f:
            data = json.load(f)
        if "api_key" in data:
            return data["api_key"]

    return None

def set_base_url(url: str):
    """Set the base URL for API calls."""
    from . import base_url as global_base_url
    global_base_url = url

def get_base_url() -> str:
    """Get the base URL for API calls."""
    from . import base_url as global_base_url
    return global_base_url if global_base_url else "https://api.uncensored.com/v1"
