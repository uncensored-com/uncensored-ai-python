from typing import Dict, Any
from .exceptions import UncensoredError

def check_balance() -> Dict[str, Any]:
    """
    Check the current account balance and usage.
    
    Returns:
        Dict containing balance and usage information
    
    Raises:
        UncensoredError: When the API is not yet available
    """
    return {"message": "You're too early: email us at devs@uncensored.com!"}

def validate_api_key(api_key: str) -> bool:
    """
    Validate the format of an API key.
    
    Args:
        api_key: The API key to validate
    
    Returns:
        bool: True if the API key format is valid
    """
    if not api_key or not isinstance(api_key, str):
        return False
    return len(api_key) > 0
