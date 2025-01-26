from typing import Dict, Any, List, Union, Iterator, Optional
from .api_config import get_api_key, get_base_url
from .exceptions import UncensoredError
from .completions import ChatCompletion
from .models import list_models
from .files import upload_dataset_file
from .fine_tuning import create_fine_tuning_job
from .images import create_image
from .utils import check_balance, validate_api_key

class Client:
    """Client for interacting with the Uncensored AI API."""
    
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize the client.
        
        Args:
            api_key: Optional API key (will try to get from config if not provided)
            base_url: Optional base URL for API calls
        """
        self.api_key = api_key or get_api_key()
        self.base_url = base_url or get_base_url()
        
        if not self.api_key or not validate_api_key(self.api_key):
            raise UncensoredError(
                "No valid API key found. Please login or set UNCENSORED_API_KEY"
            )

    def list_models(self) -> List[Dict[str, Any]]:
        """List available models."""
        return list_models()

    def create_fine_tuning_job(self, *args, **kwargs) -> Dict[str, Any]:
        """Create a fine-tuning job."""
        return create_fine_tuning_job(*args, **kwargs)

    def upload_dataset_file(
        self,
        file_path: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Upload a dataset file."""
        return upload_dataset_file(file_path, **kwargs)

    def chat_create(
        self,
        model: str,
        messages: List[Dict[str, str]],
        stream: bool = False,
        **kwargs
    ) -> Union[Dict[str, Any], Iterator[Dict[str, Any]]]:
        """Create a chat completion."""
        return ChatCompletion.create(model, messages, stream, **kwargs)

    def create_image(
        self,
        prompt: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Create an image from a prompt."""
        return create_image(prompt, **kwargs)

    def check_balance(self) -> Dict[str, Any]:
        """Check account balance and usage."""
        return check_balance()
