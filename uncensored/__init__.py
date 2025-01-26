from ._version import __version__
from .api_config import set_api_key, get_api_key, set_base_url, get_base_url
from .client import Client
from .completions import ChatCompletion
from .models import list_models
from .fine_tuning import create_fine_tuning_job
from .files import upload_dataset_file
from .images import create_image
from .utils import check_balance

# Default global placeholders
api_key = None
base_url = "https://api.uncensored.com/v1"

__all__ = [
    "__version__",
    "set_api_key",
    "get_api_key",
    "set_base_url",
    "get_base_url",
    "api_key",
    "base_url",
    "Client",
    "ChatCompletion",
    "list_models",
    "create_fine_tuning_job",
    "upload_dataset_file",
    "create_image",
    "check_balance",
]
