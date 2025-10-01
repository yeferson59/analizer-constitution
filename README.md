# Asistente Legal / Normativo (LangChain + LLMs)

Asistente inteligente para consultar leyes colombianas utilizando LangChain y múltiples proveedores de LLM.

## Características

- 🤖 **Soporte Multi-Proveedor**: OpenAI, OpenRouter, Ollama, y Groq
- 📚 **RAG (Retrieval Augmented Generation)**: Búsqueda semántica en documentos legales
- 💾 **Vector Database**: Almacenamiento eficiente con FAISS/Chroma
- 🔄 **Gestión de Memoria**: Contexto conversacional con LangChain
- 🎯 **Agentes ReAct**: Ejecución inteligente de acciones
- 📝 **Parsers Estructurados**: Respuestas en formato JSON validado
- 🖥️ **Interfaz Interactiva**: Widgets de Jupyter para demo

## Instalación

### Requisitos Previos

- Python 3.13 o superior
- uv (recomendado) o pip

### Instalar Dependencias

Con uv:
```bash
uv sync
```

Con pip:
```bash
pip install -e .
```

## Configuración

1. Copia el archivo de ejemplo de variables de entorno:
```bash
cp .env.example .env
```

2. Edita `.env` y configura las credenciales para el proveedor que desees usar:

### OpenAI
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=tu_api_key_de_openai
OPENAI_MODEL=gpt-3.5-turbo
```

### OpenRouter
```env
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=tu_api_key_de_openrouter
OPENROUTER_MODEL=google/gemini-2.0-flash-exp:free
```

### Ollama (Local)
```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

### Groq
```env
LLM_PROVIDER=groq
GROQ_API_KEY=tu_api_key_de_groq
GROQ_MODEL=llama-3.1-8b-instant
```

## Uso

### Notebook Jupyter

1. Inicia Jupyter:
```bash
jupyter notebook
```

2. Abre `main.ipynb`

3. Ejecuta las celdas en orden

### Uso Programático

```python
from llm_providers import get_llm_client

# Obtener cliente LLM (usa la configuración de .env)
llm = get_llm_client("groq")

# Usar el cliente
response = llm.invoke("¿Qué artículo protege la libertad de expresión?")
print(response.content)
```

### Cambiar de Proveedor

```python
# OpenAI
llm = get_llm_client("openai", model="gpt-4")

# OpenRouter
llm = get_llm_client("openrouter", model="anthropic/claude-3-opus")

# Ollama (local)
llm = get_llm_client("ollama", model="llama3.2")

# Groq
llm = get_llm_client("groq", model="mixtral-8x7b-32768")
```

## Arquitectura

El proyecto utiliza una arquitectura modular:

- **`llm_providers.py`**: Módulo con clases para diferentes proveedores LLM
  - `BaseLLMProvider`: Clase base abstracta
  - `OpenAIProvider`: Implementación para OpenAI
  - `OpenRouterProvider`: Implementación para OpenRouter
  - `OllamaProvider`: Implementación para Ollama
  - `GroqProvider`: Implementación para Groq
  - `LLMProviderFactory`: Factory para crear proveedores

- **`main.ipynb`**: Notebook principal con toda la funcionalidad
  - Loaders de documentos (PDF, TXT, MD)
  - Transformadores y splitters
  - Embeddings y Vector DB
  - Pipeline RAG
  - Agentes ReAct
  - Interfaz con widgets

## Documentos de Ejemplo

Los documentos legales de ejemplo están en la carpeta `data/`:
- Constitución Política de Colombia (1991)
- Reglamento académico de pregrado

## Desarrollo

### Estructura del Proyecto

```
.
├── main.ipynb              # Notebook principal
├── llm_providers.py        # Módulo de proveedores LLM
├── data/                   # Documentos legales
├── pyproject.toml          # Configuración del proyecto
├── .env.example            # Plantilla de variables de entorno
├── ROADMAP.md             # Plan del proyecto
└── README.md              # Este archivo
```

### Agregar un Nuevo Proveedor

1. Crear una nueva clase heredando de `BaseLLMProvider`
2. Implementar los métodos abstractos
3. Registrar en `LLMProviderFactory.PROVIDERS`
4. Actualizar `.env.example` con las variables necesarias

## Limitaciones

- Los resultados deben ser verificados por profesionales legales
- La cobertura depende de los documentos indexados
- Requiere API key válida o servidor Ollama local
- Los modelos pueden tener limitaciones de contexto

## Licencia

Este proyecto es para fines educativos.

## Contribuidores

Proyecto desarrollado para el curso de LangChain y LLMs.
