# 🏛️ Asistente Legal Colombiano (LangChain + LLMs)

Sistema inteligente para consultar la Constitución Política de Colombia y documentos normativos utilizando RAG, agentes ReAct y múltiples proveedores de LLM.

## ✨ Características Principales

- 🤖 **Soporte Multi-Proveedor**: OpenAI, OpenRouter, Ollama, y Groq
- 📚 **RAG (Retrieval Augmented Generation)**: Búsqueda semántica avanzada
- � **Vector Database**: Chroma con embeddings de OpenAI
- 🔄 **Gestión de Memoria**: Contexto conversacional persistente
- � **Agentes ReAct**: Razonamiento y selección automática de herramientas
- 📝 **Parsers Estructurados**: Respuestas validadas con JSON schema
- 🎨 **Interfaz Interactiva**: UI completa con Jupyter widgets
- 🧪 **Tests Automatizados**: Suite de smoke tests incluida
- 📄 **Múltiples Loaders**: Soporte para PDF, TXT, MD y URLs
- 🤖 **Sintetizador**: Generación automática de resúmenes

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
OPENROUTER_MODEL=google/gemini-2.5-flash-preview-09-2025
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

## 📊 Estado del Proyecto

**✅ PROYECTO 100% COMPLETO - LISTO PARA PRESENTACIÓN**

### Requisitos Implementados (7/7)

| #   | Requisito              | Estado |
| --- | ---------------------- | ------ |
| a   | Mensajes y plantillas  | ✅     |
| b   | Parsers de salida      | ✅     |
| c   | Loaders (local/URLs)   | ✅     |
| d   | Vector DB + RAG        | ✅     |
| e   | Gestión de memoria     | ✅     |
| f   | Agentes ReAct          | ✅     |
| g   | Transformación de docs | ✅     |

### Componentes Adicionales

- ✅ Interfaz de usuario completa con widgets
- ✅ Suite de 8 tests automatizados
- ✅ Loader desde URLs con BeautifulSoup
- ✅ Sintetizador de resúmenes automáticos
- ✅ Modo debug para razonamiento del agente
- ✅ Panel de estadísticas del sistema
- ✅ Soporte multi-proveedor (4 LLMs)

### Documentación Completa

- ✅ `ARCHITECTURE.md` - Diagrama de arquitectura completo
- ✅ `PRESENTATION_SCRIPT.md` - Script de presentación de 5 minutos
- ✅ `DEMO_QUESTIONS.md` - Preguntas preparadas para la demo
- ✅ `QUICK_START.md` - Guía rápida de ejecución
- ✅ `FINAL_CHECKLIST.md` - Checklist ejecutivo
- ✅ `IMPLEMENTATION_SUMMARY.md` - Resumen técnico
- ✅ `ROADMAP.md` - Plan y progreso del proyecto
- ✅ `MIGRATION_GUIDE.md` - Guía de migración
- ✅ `CHANGELOG.md` - Registro de cambios

## 🚀 Quick Start para la Demo

### 1. Configurar (una sola vez)

```bash
# Clonar y entrar al directorio
cd analizer-constitution

# Instalar dependencias
uv sync

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tu API key
```

### 2. Ejecutar Notebook

```bash
# Abrir en Jupyter o VS Code
jupyter notebook main.ipynb

# O en VS Code:
code main.ipynb
```

### 3. Ejecutar Celdas en Orden

1. Celda 3: Imports y configuración LLM ✅
2. Celda 4: Loaders ✅
3. Celda 5: Preprocesamiento y chunks ✅
4. Celda 6: **Vector Database** (⚠️ importante, tarda 1-2 min) ✅
5. Celda 7-12: Parsers, memoria, agente ✅
6. Celda 13: **Interfaz de Usuario** (para la demo) ⭐
7. Celda 14: Tests automatizados ✅

### 4. Hacer Demo

En la celda 13 (UI), probar con:

**Pregunta legal (usa RAG):**

```
¿Qué artículo de la Constitución protege la libertad de expresión?
```

**Pregunta general (usa LLM):**

```
Explica brevemente qué es el habeas corpus
```

## 📚 Documentación Adicional

- **Arquitectura detallada**: Ver `ARCHITECTURE.md`
- **Script de presentación**: Ver `PRESENTATION_SCRIPT.md`
- **Preguntas para demo**: Ver `DEMO_QUESTIONS.md`
- **Guía rápida**: Ver `QUICK_START.md`
- **Checklist completo**: Ver `FINAL_CHECKLIST.md`

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
