from typing import Dict, Any, Optional

def create_fine_tuning_job(
    training_file: str,
    model: str = "model-t",
    validation_file: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Create a fine-tuning job.
    
    Args:
        training_file: ID of the training data file
        model: Base model to fine-tune
        validation_file: Optional validation data file ID
        **kwargs: Additional parameters for fine-tuning
    
    Returns:
        Dict containing job information
    """
    return {
        "id": "ft-placeholder",
        "status": "not_available",
        "message": "You're too early: email us at devs@uncensored.com!"
    }

def list_fine_tuning_jobs() -> Dict[str, Any]:
    """List all fine-tuning jobs."""
    return {
        "jobs": [],
        "message": "You're too early: email us at devs@uncensored.com!"
    }
