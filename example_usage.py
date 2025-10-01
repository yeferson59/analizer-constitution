#!/usr/bin/env python3
"""
Example usage of the LLM providers module.

This script demonstrates how to use different LLM providers in your application.
"""

import os
from dotenv import load_dotenv
from llm_providers import get_llm_client, LLMProviderFactory

# Load environment variables
load_dotenv()

def example_basic_usage():
    """Example 1: Basic usage with default provider."""
    print("=" * 60)
    print("Example 1: Basic Usage")
    print("=" * 60)
    
    # Get the default provider from environment
    provider = os.getenv('LLM_PROVIDER', 'groq')
    print(f"Using provider: {provider}\n")
    
    try:
        # Initialize LLM client
        llm = get_llm_client(provider)
        print(f"✅ LLM client initialized successfully!\n")
        
        # Make a simple query (requires valid API key)
        # response = llm.invoke("¿Qué es la Constitución de Colombia?")
        # print(f"Response: {response.content}")
        
    except Exception as e:
        print(f"⚠️  Error: {e}")
        print("Note: Make sure to set the appropriate API key in your .env file\n")


def example_explicit_provider():
    """Example 2: Explicitly choose a provider."""
    print("=" * 60)
    print("Example 2: Explicit Provider Selection")
    print("=" * 60)
    
    # List available providers
    providers = LLMProviderFactory.get_available_providers()
    print(f"Available providers: {', '.join(providers)}\n")
    
    # Example with each provider (commented out to avoid API calls)
    examples = [
        ("openai", "gpt-3.5-turbo"),
        ("openrouter", "google/gemini-2.0-flash-exp:free"),
        ("ollama", "llama3.2"),
        ("groq", "llama-3.1-8b-instant"),
    ]
    
    for provider_name, model in examples:
        print(f"Provider: {provider_name}, Model: {model}")
        try:
            llm = get_llm_client(provider_name, model=model)
            print(f"  ✅ {provider_name} client created successfully")
        except Exception as e:
            print(f"  ⚠️  {provider_name}: {e}")
    
    print()


def example_custom_configuration():
    """Example 3: Custom configuration for providers."""
    print("=" * 60)
    print("Example 3: Custom Configuration")
    print("=" * 60)
    
    # OpenAI with custom parameters
    print("OpenAI with temperature=0.7:")
    try:
        llm = get_llm_client("openai", model="gpt-3.5-turbo", temperature=0.7)
        print("  ✅ Created with custom temperature")
    except Exception as e:
        print(f"  ⚠️  Error: {e}")
    
    # Ollama with custom base URL
    print("\nOllama with custom base URL:")
    try:
        llm = get_llm_client("ollama", model="llama3.2", base_url="http://localhost:11434")
        print("  ✅ Created with custom base URL")
    except Exception as e:
        print(f"  ⚠️  Error: {e}")
    
    # OpenRouter with custom headers
    print("\nOpenRouter with custom configuration:")
    try:
        llm = get_llm_client(
            "openrouter", 
            model="anthropic/claude-3-opus",
            temperature=0.5
        )
        print("  ✅ Created with custom model and temperature")
    except Exception as e:
        print(f"  ⚠️  Error: {e}")
    
    print()


def example_factory_pattern():
    """Example 4: Using the factory pattern directly."""
    print("=" * 60)
    print("Example 4: Factory Pattern")
    print("=" * 60)
    
    try:
        # Create provider instance
        from llm_providers import GroqProvider
        provider = GroqProvider(api_key=os.getenv("GROQ_API_KEY", "dummy"))
        
        print(f"Provider name: {provider.get_provider_name()}")
        print(f"Model: {provider.model}")
        
        # Get the actual client
        # client = provider.get_client()
        print("✅ Provider instance created successfully\n")
        
    except Exception as e:
        print(f"⚠️  Error: {e}\n")


def main():
    """Run all examples."""
    print("\n")
    print("=" * 60)
    print("LLM Providers - Usage Examples")
    print("=" * 60)
    print("\nNote: These examples demonstrate the API structure.")
    print("To make actual LLM calls, ensure you have valid API keys in .env\n")
    
    example_basic_usage()
    example_explicit_provider()
    example_custom_configuration()
    example_factory_pattern()
    
    print("=" * 60)
    print("Examples completed!")
    print("=" * 60)
    print("\nTo use in your code:")
    print("  from llm_providers import get_llm_client")
    print("  llm = get_llm_client('groq')")
    print("  response = llm.invoke('Your question here')")
    print()


if __name__ == '__main__':
    main()
