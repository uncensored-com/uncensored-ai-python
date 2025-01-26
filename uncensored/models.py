from typing import List, Dict, Any

def list_models() -> List[Dict[str, Any]]:
    """
    List all available models.
    
    Returns:
        List of model information dictionaries
    """
    return [
        {
            "id": "model-t",
            "name": "model t - latest",
            "status": "coming_soon",
            "message": "You're too early: email us at devs@uncensored.com!"
        }
    ]

def get_model_details(model_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific model.
    
    Args:
        model_id: The ID of the model to get details for
    
    Returns:
        Dict containing model details
    """
    return {
        "id": model_id,
        "status": "coming_soon",
        "message": "You're too early: email us at devs@uncensored.com!"
    }
