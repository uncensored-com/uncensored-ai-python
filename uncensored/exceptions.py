class UncensoredError(Exception):
    """Base exception for uncensored errors."""
    pass

class AuthenticationError(UncensoredError):
    """Raised when authentication fails."""
    pass

class APIError(UncensoredError):
    """Raised when the API returns an error."""
    pass

class InvalidRequestError(UncensoredError):
    """Raised when the request is invalid."""
    pass
