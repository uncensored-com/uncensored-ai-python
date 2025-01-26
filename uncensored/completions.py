from typing import Dict, Any, List, Union, Iterator
from .retries import exponential_backoff_retry

class ChatCompletion:
    @staticmethod
    def create(
        model: str,
        messages: List[Dict[str, str]],
        stream: bool = False,
        temperature: float = 1.0,
        max_tokens: int = None,
        **kwargs
    ) -> Union[Dict[str, Any], Iterator[Dict[str, Any]]]:
        """
        Create a chat completion.
        
        Args:
            model: ID of the model to use
            messages: List of message dictionaries
            stream: Whether to stream the response
            temperature: Sampling temperature
            max_tokens: Maximum tokens in the response
            **kwargs: Additional parameters
        
        Returns:
            Dict or Iterator of response chunks if streaming
        """
        def _make_request():
            # Placeholder for actual API request
            if not stream:
                return {
                    "id": "chatcmpl-placeholder",
                    "object": "chat.completion",
                    "created": 0,
                    "choices": [{
                        "index": 0,
                        "message": {
                            "role": "assistant",
                            "content": "You're too early: email us at devs@uncensored.com!"
                        }
                    }]
                }
            else:
                return ChatCompletion._stream_response()

        return exponential_backoff_retry(_make_request)

    @staticmethod
    def _stream_response() -> Iterator[Dict[str, Any]]:
        """Generate streaming response chunks."""
        message = "You're too early: email us at devs@uncensored.com!"
        words = message.split()
        
        for i, word in enumerate(words):
            yield {
                "id": f"chatcmpl-placeholder-{i}",
                "object": "chat.completion.chunk",
                "created": 0,
                "choices": [{
                    "index": 0,
                    "delta": {
                        "content": word + " "
                    }
                }]
            }
