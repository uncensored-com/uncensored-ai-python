from typing import Dict, Any, List, Union

def create_image(
    prompt: str,
    model: str = "dall-e-2",
    n: int = 1,
    size: str = "1024x1024",
    response_format: str = "url",
    **kwargs
) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """
    Create an image given a prompt.
    
    Args:
        prompt: Text description of the desired image
        model: Model to use for image generation
        n: Number of images to generate
        size: Size of the generated images
        response_format: Format of the response ("url" or "b64_json")
        **kwargs: Additional parameters
    
    Returns:
        Dict containing image URLs or base64 data
    """
    return {
        "created": 0,
        "data": [{"url": "You're too early: email us at devs@uncensored.com!"}] * n
    }
