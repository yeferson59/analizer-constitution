# Migration Guide: Multi-Provider LLM Support

## Overview

This project has been refactored to support multiple LLM providers through a clean, class-based architecture. This guide explains the changes and how to use the new system.

## What Changed?

### Before

```python
# Old way - hardcoded provider
from langchain_groq import ChatGroq
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)
```

### After

```python
# New way - flexible provider selection
from llm_providers import get_llm_client

# Provider configured in .env file
llm = get_llm_client(os.getenv('LLM_PROVIDER', 'groq'))
```

## Benefits

1. **Flexibility**: Switch providers by changing one environment variable
2. **Clean Code**: No more commented-out provider code
3. **Extensibility**: Easy to add new providers
4. **Consistency**: Unified interface across all providers
5. **Maintainability**: Single source of truth for LLM initialization

## Quick Start

### 1. Update Your `.env` File

Choose your preferred provider and set the appropriate variables:

```bash
# Choose one provider
LLM_PROVIDER=groq

# Set the corresponding API key
GROQ_API_KEY=your_api_key_here
```

### 2. Use in Your Code

The notebook now automatically uses the configured provider:

```python
from llm_providers import get_llm_client

# Get LLM client based on environment configuration
llm = get_llm_client(os.getenv('LLM_PROVIDER', 'groq'))

# Use normally
response = llm.invoke("Your question here")
```

## Supported Providers

### OpenAI

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-3.5-turbo  # optional
```

**Use Cases:**

- Production applications
- High-quality responses
- Latest GPT models

### OpenRouter

```env
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=sk-or-...
OPENROUTER_MODEL=google/gemini-2.5-flash-preview-09-2025  # optional
```

**Use Cases:**

- Access to multiple model providers (Anthropic, Google, Meta, etc.)
- Cost optimization
- Model comparison

### Ollama (Local)

```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2  # optional
```

**Use Cases:**

- Privacy-sensitive applications
- Offline development
- No API costs
- Full control over models

### Groq

```env
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_...
GROQ_MODEL=llama-3.1-8b-instant  # optional
```

**Use Cases:**

- Fast inference
- Cost-effective
- Open-source models

## Advanced Usage

### Switching Providers Programmatically

```python
from llm_providers import get_llm_client

# Use different providers in the same code
groq_llm = get_llm_client("groq")
openai_llm = get_llm_client("openai", model="gpt-4")
local_llm = get_llm_client("ollama", model="llama3.2")
```

### Custom Configuration

```python
from llm_providers import get_llm_client

# Pass additional parameters
llm = get_llm_client(
    "openai",
    model="gpt-4",
    temperature=0.7,
    max_tokens=2000
)
```

### Using the Factory Pattern

```python
from llm_providers import LLMProviderFactory

# Create provider instance
provider = LLMProviderFactory.create_provider(
    "groq",
    model="mixtral-8x7b-32768"
)

# Get the client
llm = provider.get_client()
```

## Common Tasks

### Task: Switch from Groq to OpenAI

1. Update `.env`:

   ```bash
   LLM_PROVIDER=openai
   OPENAI_API_KEY=sk-...
   ```

2. Restart notebook kernel

3. Run cells - no code changes needed!

### Task: Test Multiple Providers

```python
from llm_providers import LLMProviderFactory

question = "¿Qué es la Constitución de Colombia?"

for provider in LLMProviderFactory.get_available_providers():
    try:
        llm = get_llm_client(provider)
        response = llm.invoke(question)
        print(f"{provider}: {response.content[:100]}...")
    except Exception as e:
        print(f"{provider}: {e}")
```

### Task: Use Ollama for Development, Groq for Production

```python
import os

# Development
if os.getenv('ENV') == 'development':
    llm = get_llm_client('ollama')
# Production
else:
    llm = get_llm_client('groq')
```

## Troubleshooting

### Error: "Provider API key is required"

**Solution:** Set the appropriate API key in your `.env` file:

```bash
# For Groq
GROQ_API_KEY=your_key_here

# For OpenAI
OPENAI_API_KEY=your_key_here

# etc.
```

### Error: "Unsupported provider"

**Solution:** Check available providers:

```python
from llm_providers import LLMProviderFactory
print(LLMProviderFactory.get_available_providers())
```

### Error: "ModuleNotFoundError: No module named 'langchain_groq'"

**Solution:** Install missing dependencies:

```bash
pip install langchain-groq langchain-ollama
# or
uv sync
```

### Ollama Connection Error

**Solution:** Ensure Ollama is running:

```bash
ollama serve
```

## Backward Compatibility

The changes are **100% backward compatible**. Your existing notebook cells will work without modification because:

1. The LLM initialization cell now uses the provider system
2. All other cells that use `llm` variable work the same way
3. The LLM client interface is identical across providers

## Files Changed

- ✅ `llm_providers.py` - **NEW**: Provider implementations
- ✅ `main.ipynb` - Updated LLM initialization, removed redundant cells
- ✅ `pyproject.toml` - Added provider dependencies
- ✅ `.env.example` - Added all provider configurations
- ✅ `README.md` - Updated documentation
- ✅ `ROADMAP.md` - Updated project status

## Need Help?

Check these resources:

- `README.md` - General documentation
- `example_usage.py` - Working examples
- `CHANGELOG.md` - Detailed change list
- `.env.example` - Configuration examples

## Next Steps

1. ✅ Choose your preferred provider
2. ✅ Configure `.env` file
3. ✅ Run the notebook
4. ✅ Start building!

Happy coding! 🚀
