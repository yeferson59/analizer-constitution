"""
LLM Provider Classes for supporting multiple LLM providers.

This module provides a unified interface for different LLM providers:
- OpenAI
- OpenRouter (uses OpenAI-compatible API)
- Ollama
- Groq
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import os


class BaseLLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    def __init__(self, model: str, api_key: Optional[str] = None, **kwargs):
        """
        Initialize the LLM provider.
        
        Args:
            model: The model name/identifier
            api_key: API key for the provider (if required)
            **kwargs: Additional provider-specific arguments
        """
        self.model = model
        self.api_key = api_key
        self.kwargs = kwargs
        self._client = None
    
    @abstractmethod
    def get_client(self):
        """Return the initialized LLM client."""
        pass
    
    @abstractmethod
    def get_provider_name(self) -> str:
        """Return the provider name."""
        pass


class OpenAIProvider(BaseLLMProvider):
    """OpenAI LLM Provider."""
    
    def __init__(self, model: str = "gpt-3.5-turbo", api_key: Optional[str] = None, **kwargs):
        """
        Initialize OpenAI provider.
        
        Args:
            model: OpenAI model name (default: gpt-3.5-turbo)
            api_key: OpenAI API key (default: from OPENAI_API_KEY env var)
            **kwargs: Additional arguments for ChatOpenAI
        """
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable.")
        super().__init__(model, api_key, **kwargs)
    
    def get_client(self):
        """Return initialized ChatOpenAI client."""
        if self._client is None:
            from langchain_openai import ChatOpenAI
            self._client = ChatOpenAI(
                model=self.model,
                api_key=self.api_key,
                **self.kwargs
            )
        return self._client
    
    def get_provider_name(self) -> str:
        return "OpenAI"


class OpenRouterProvider(BaseLLMProvider):
    """OpenRouter LLM Provider (uses OpenAI-compatible API)."""
    
    def __init__(self, model: str = "google/gemini-2.5-flash-preview-09-2025", api_key: Optional[str] = None, **kwargs):
        """
        Initialize OpenRouter provider.
        
        Args:
            model: OpenRouter model name (default: google/gemini-2.5-flash-preview-09-2025)
            api_key: OpenRouter API key (default: from OPENROUTER_API_KEY env var)
            **kwargs: Additional arguments for ChatOpenAI
        """
        api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OpenRouter API key is required. Set OPENROUTER_API_KEY environment variable.")
        
        # OpenRouter uses OpenAI-compatible API with custom base_url
        kwargs["base_url"] = kwargs.get("base_url", "https://openrouter.ai/api/v1")
        super().__init__(model, api_key, **kwargs)
    
    def get_client(self):
        """Return initialized ChatOpenAI client configured for OpenRouter."""
        if self._client is None:
            from langchain_openai import ChatOpenAI
            self._client = ChatOpenAI(
                model=self.model,
                api_key=self.api_key,
                temperature=0.1,
                top_p=0.20,
                **self.kwargs
            )
        return self._client
    
    def get_provider_name(self) -> str:
        return "OpenRouter"


class OllamaProvider(BaseLLMProvider):
    """Ollama LLM Provider for local models."""
    
    def __init__(self, model: str = "llama3.2", base_url: Optional[str] = None, **kwargs):
        """
        Initialize Ollama provider.
        
        Args:
            model: Ollama model name (default: llama3.2)
            base_url: Ollama server URL (default: from OLLAMA_BASE_URL env var or http://localhost:11434)
            **kwargs: Additional arguments for ChatOllama
        """
        base_url = base_url or os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        kwargs["base_url"] = base_url
        super().__init__(model, api_key=None, **kwargs)
    
    def get_client(self):
        """Return initialized ChatOllama client."""
        if self._client is None:
            try:
                from langchain_ollama import ChatOllama
            except ImportError:
                raise ImportError(
                    "langchain-ollama is required for Ollama provider. "
                    "Install it with: pip install langchain-ollama"
                )
            self._client = ChatOllama(
                model=self.model,
                **self.kwargs
            )
        return self._client
    
    def get_provider_name(self) -> str:
        return "Ollama"


class GroqProvider(BaseLLMProvider):
    """Groq LLM Provider."""
    
    def __init__(self, model: str = "llama-3.1-8b-instant", api_key: Optional[str] = None, **kwargs):
        """
        Initialize Groq provider.
        
        Args:
            model: Groq model name (default: llama-3.1-8b-instant)
            api_key: Groq API key (default: from GROQ_API_KEY env var)
            **kwargs: Additional arguments for ChatGroq
        """
        api_key = api_key or os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("Groq API key is required. Set GROQ_API_KEY environment variable.")
        super().__init__(model, api_key, **kwargs)
    
    def get_client(self):
        """Return initialized ChatGroq client."""
        if self._client is None:
            try:
                from langchain_groq import ChatGroq
            except ImportError:
                raise ImportError(
                    "langchain-groq is required for Groq provider. "
                    "Install it with: pip install langchain-groq"
                )
            self._client = ChatGroq(
                model=self.model,
                api_key=self.api_key,
                **self.kwargs
            )
        return self._client
    
    def get_provider_name(self) -> str:
        return "Groq"


class LLMProviderFactory:
    """Factory class to create LLM providers."""
    
    PROVIDERS = {
        "openai": OpenAIProvider,
        "openrouter": OpenRouterProvider,
        "ollama": OllamaProvider,
        "groq": GroqProvider,
    }
    
    @classmethod
    def create_provider(cls, provider_name: str, model: Optional[str] = None, **kwargs) -> BaseLLMProvider:
        """
        Create an LLM provider instance.
        
        Args:
            provider_name: Name of the provider (openai, openrouter, ollama, groq)
            model: Model name (optional, uses provider default if not specified)
            **kwargs: Additional provider-specific arguments
            
        Returns:
            BaseLLMProvider instance
            
        Raises:
            ValueError: If provider_name is not supported
        """
        provider_name = provider_name.lower()
        if provider_name not in cls.PROVIDERS:
            raise ValueError(
                f"Unsupported provider: {provider_name}. "
                f"Supported providers: {', '.join(cls.PROVIDERS.keys())}"
            )
        
        provider_class = cls.PROVIDERS[provider_name]
        if model:
            kwargs["model"] = model
        return provider_class(**kwargs)
    
    @classmethod
    def get_available_providers(cls) -> list:
        """Return list of available provider names."""
        return list(cls.PROVIDERS.keys())


def get_llm_client(provider: str = "openai", model: Optional[str] = None, **kwargs):
    """
    Convenience function to get an LLM client.
    
    Args:
        provider: Provider name (openai, openrouter, ollama, groq)
        model: Model name (optional)
        **kwargs: Additional provider-specific arguments
        
    Returns:
        LangChain chat model instance
        
    Example:
        >>> llm = get_llm_client("groq", model="llama-3.1-8b-instant")
        >>> response = llm.invoke("Hello, how are you?")
    """
    provider_instance = LLMProviderFactory.create_provider(provider, model, **kwargs)
    return provider_instance.get_client()
