"""
Core provider interface for AgnosticAgentFramework.
Defines the contract that all model providers must implement.
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass


class ModelRole(Enum):
    """Defines standard roles for model interactions."""
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    FUNCTION = "function"
    TOOL = "tool"


@dataclass
class ModelMessage:
    """Represents a standard message format across providers."""
    role: ModelRole
    content: Union[str, List[Dict[str, Any]]]
    name: Optional[str] = None
    function_call: Optional[Dict[str, Any]] = None
    tool_calls: Optional[List[Dict[str, Any]]] = None


@dataclass
class ModelCapabilities:
    """Defines the capabilities of a specific model."""
    max_context_length: int
    supports_functions: bool
    supports_vision: bool
    supports_streaming: bool
    supports_tools: bool
    input_modalities: List[str]
    output_modalities: List[str]


class ModelProvider(ABC):
    """
    Abstract base class for model providers.
    Implements the core interface that all providers must support.
    """

    @abstractmethod
    async def initialize(self, **kwargs) -> None:
        """Initialize the provider with necessary credentials and configuration."""
        pass

    @abstractmethod
    async def validate_credentials(self) -> bool:
        """Validate that the provider credentials are correct and active."""
        pass

    @abstractmethod
    async def get_available_models(self) -> List[str]:
        """Retrieve list of available models from the provider."""
        pass

    @abstractmethod
    async def get_model_capabilities(self, model: str) -> ModelCapabilities:
        """Get the capabilities of a specific model."""
        pass

    @abstractmethod
    async def generate_completion(
        self,
        messages: List[ModelMessage],
        model: str,
        temperature: float = 1.0,
        max_tokens: Optional[int] = None,
        stream: bool = False,
        tools: Optional[List[Dict[str, Any]]] = None,
        response_format: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Union[Dict[str, Any], AsyncIterator[Dict[str, Any]]]:
        """
        Generate a completion from the model.
        
        Args:
            messages: List of messages in the conversation
            model: Model identifier to use
            temperature: Sampling temperature (0-2)
            max_tokens: Maximum tokens to generate
            stream: Whether to stream the response
            tools: List of tools/functions available to the model
            response_format: Desired format of the response
            **kwargs: Additional provider-specific parameters
            
        Returns:
            Model response as a dict or async iterator if streaming
        """
        pass

    @abstractmethod
    async def generate_embeddings(
        self,
        texts: Union[str, List[str]],
        model: str,
        **kwargs
    ) -> List[List[float]]:
        """
        Generate embeddings for provided texts.
        
        Args:
            texts: Single text or list of texts to embed
            model: Model identifier to use
            **kwargs: Additional provider-specific parameters
            
        Returns:
            List of embedding vectors
        """
        pass

    @abstractmethod
    async def count_tokens(
        self,
        text: str,
        model: str
    ) -> int:
        """
        Count the number of tokens in the text for the specified model.
        
        Args:
            text: Text to count tokens for
            model: Model identifier to use
            
        Returns:
            Number of tokens
        """
        pass

    async def validate_response(
        self,
        response: Dict[str, Any]
    ) -> bool:
        """
        Validate that a model response contains expected fields and format.
        
        Args:
            response: Response from the model to validate
            
        Returns:
            True if response is valid, False otherwise
        """
        required_fields = {"id", "created", "model", "choices"}
        return all(field in response for field in required_fields)

    async def handle_error(
        self,
        error: Exception
    ) -> None:
        """
        Handle provider-specific errors in a standardized way.
        
        Args:
            error: Exception that occurred
            
        Raises:
            Standardized framework exception
        """
        # Default implementation logs the error
        # Specific providers should override with their error mapping
        raise NotImplementedError(
            f"Provider must implement error handling for {error.__class__.__name__}"
        )

    @abstractmethod
    async def close(self) -> None:
        """Clean up provider resources."""
        pass


class ProviderException(Exception):
    """Base exception class for provider-related errors."""
    pass


class ProviderAuthenticationError(ProviderException):
    """Raised when provider authentication fails."""
    pass


class ProviderAPIError(ProviderException):
    """Raised when the provider API returns an error."""
    pass


class ProviderRateLimitError(ProviderException):
    """Raised when provider rate limits are exceeded."""
    pass


class ProviderInvalidRequestError(ProviderException):
    """Raised when the request to the provider is invalid."""
    pass
