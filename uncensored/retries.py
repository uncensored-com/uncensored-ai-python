import time
import random
from typing import Callable, TypeVar, Any

T = TypeVar('T')

def exponential_backoff_retry(
    request_func: Callable[[], T],
    max_retries: int = 3,
    base_delay: float = 1.0,
    factor: float = 2.0
) -> T:
    """
    Execute a function with exponential backoff retry logic.
    
    Args:
        request_func: Function to execute
        max_retries: Maximum number of retry attempts
        base_delay: Initial delay between retries in seconds
        factor: Multiplication factor for subsequent delays
    
    Returns:
        The result of the request_func call
    
    Raises:
        Exception: The last exception encountered after all retries
    """
    attempt = 0
    while True:
        try:
            return request_func()
        except Exception as e:
            attempt += 1
            if attempt > max_retries:
                raise e

            sleep_time = base_delay * (factor ** (attempt - 1))
            sleep_time += random.uniform(0, 0.5)  # Add jitter
            time.sleep(sleep_time)
