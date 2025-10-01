# 🏗️ Arquitectura del Sistema - Asistente Legal Colombiano

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ASISTENTE LEGAL COLOMBIANO                           │
│                   (LangChain + Multi-Provider LLM)                      │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                        1. CAPA DE ENTRADA                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                 │
│  │   Jupyter    │  │  FileUpload  │  │   URL Input  │                 │
│  │   Widgets    │  │    Widget    │  │    Widget    │                 │
│  │   (UI Main)  │  │   (Local)    │  │   (Remote)   │                 │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                 │
│         │                  │                  │                          │
│         └──────────────────┴──────────────────┘                          │
│                            │                                             │
│                    User Questions                                        │
│                            ↓                                             │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                     2. CAPA DE LOADERS                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                 │
│  │   PyPDF2     │  │  Text Files  │  │ BeautifulSoup│                 │
│  │  (PDF Parser)│  │  (.txt, .md) │  │ (HTML Parser)│                 │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                 │
│         │                  │                  │                          │
│         └──────────────────┴──────────────────┘                          │
│                            │                                             │
│                    Raw Document Text                                     │
│                            ↓                                             │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                  3. CAPA DE TRANSFORMACIÓN                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   RecursiveCharacterTextSplitter                       │            │
│  │   - chunk_size: 1000                                   │            │
│  │   - chunk_overlap: 200                                 │            │
│  └────────────────────┬───────────────────────────────────┘            │
│                       │                                                  │
│                       ↓                                                  │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   DOCUMENT_CHUNKS (1000+ chunks)                       │            │
│  │   {source, chunk_index, text, metadata}                │            │
│  └────────────────────┬───────────────────────────────────┘            │
│                       │                                                  │
│                       ↓                                                  │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   Sintetizador (Opcional)                              │            │
│  │   - Genera resúmenes con LLM                           │            │
│  └────────────────────────────────────────────────────────┘            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                  4. CAPA DE EMBEDDINGS                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   OpenAI Embeddings API                                │            │
│  │   - Model: text-embedding-ada-002                      │            │
│  │   - Dimensions: 1536                                   │            │
│  └────────────────────┬───────────────────────────────────┘            │
│                       │                                                  │
│                       ↓                                                  │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   Chroma Vector Database                               │            │
│  │   - Persistent storage: ./chroma_db                    │            │
│  │   - Similarity search (cosine)                         │            │
│  │   - Top-k retrieval (k=4)                              │            │
│  └────────────────────────────────────────────────────────┘            │
│                                                                          │
│                       ↓ [Fallback]                                       │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   Keyword Search (Backup)                              │            │
│  │   - Simple string matching                             │            │
│  │   - Word frequency scoring                             │            │
│  └────────────────────────────────────────────────────────┘            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                    5. CAPA DE RECUPERACIÓN (RAG)                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│                    User Query                                            │
│                       │                                                  │
│                       ↓                                                  │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   retrieve(query, k=4)                                 │            │
│  │   - Similarity search in vectordb                      │            │
│  │   - Returns top-k relevant chunks                      │            │
│  └────────────────────┬───────────────────────────────────┘            │
│                       │                                                  │
│                       ↓                                                  │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   rag_answer(query, k=4)                               │            │
│  │   1. Retrieve relevant chunks                          │            │
│  │   2. Build context from chunks                         │            │
│  │   3. Create prompt with context                        │            │
│  │   4. Call LLM                                          │            │
│  │   5. Return {answer, citations}                        │            │
│  └────────────────────────────────────────────────────────┘            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                  6. CAPA DE LLM (Multi-Provider)                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │
│  │    Groq      │  │   OpenAI     │  │ OpenRouter   │  │  Ollama    │ │
│  │  (Default)   │  │              │  │              │  │  (Local)   │ │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤  ├────────────┤ │
│  │ llama-3.1-   │  │ gpt-3.5-     │  │ Compatible   │  │ llama2     │ │
│  │ 70b-versatile│  │ turbo        │  │ with OpenAI  │  │ mistral    │ │
│  │ mixtral-8x7b │  │ gpt-4        │  │ API          │  │ etc.       │ │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬─────┘ │
│         │                  │                  │                 │        │
│         └──────────────────┴──────────────────┴─────────────────┘        │
│                            │                                             │
│                   LLMProviderFactory                                     │
│                            ↓                                             │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   llm_call(prompt) → response                          │            │
│  └────────────────────────────────────────────────────────┘            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                    7. CAPA DE MEMORIA                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   ConversationBufferMemory                             │            │
│  │   - Stores conversation history                        │            │
│  │   - Maintains context across turns                     │            │
│  │   - Memory key: "history"                              │            │
│  └────────────────────────────────────────────────────────┘            │
│                                                                          │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   conversation_history[]                               │            │
│  │   - UI-level history tracking                          │            │
│  │   - Timestamps and metadata                            │            │
│  └────────────────────────────────────────────────────────┘            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                    8. CAPA DE AGENTE (ReAct)                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   ReAct Agent (ZERO_SHOT_REACT_DESCRIPTION)           │            │
│  │                                                        │            │
│  │   Thought → Action → Observation → Repeat              │            │
│  └────────────────────┬───────────────────────────────────┘            │
│                       │                                                  │
│       ┌───────────────┴───────────────┐                                │
│       │                               │                                │
│       ↓                               ↓                                │
│  ┌─────────────────┐         ┌──────────────────┐                     │
│  │ BusquedaLegalRAG│         │ RespuestaDirecta │                     │
│  │ (Tool 1)        │         │ (Tool 2)         │                     │
│  ├─────────────────┤         ├──────────────────┤                     │
│  │ - Uses RAG      │         │ - Direct LLM     │                     │
│  │ - Searches docs │         │ - No retrieval   │                     │
│  │ - Returns       │         │ - General        │                     │
│  │   citations     │         │   knowledge      │                     │
│  └─────────────────┘         └──────────────────┘                     │
│                                                                          │
│  Decision Logic:                                                         │
│  - Legal/specific question → Tool 1 (RAG)                               │
│  - General/conceptual question → Tool 2 (Direct)                        │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                   9. CAPA DE PARSERS                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   StructuredOutputParser                               │            │
│  │                                                        │            │
│  │   Response Schema:                                     │            │
│  │   {                                                    │            │
│  │     "answer": "string",                                │            │
│  │     "citations": [                                     │            │
│  │       {                                                │            │
│  │         "source": "filename",                          │            │
│  │         "chunk_index": 0,                              │            │
│  │         "score": 0.95                                  │            │
│  │       }                                                │            │
│  │     ],                                                 │            │
│  │     "follow_up": false                                 │            │
│  │   }                                                    │            │
│  └────────────────────────────────────────────────────────┘            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                   10. CAPA DE SALIDA                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   UI Output Widget                                     │            │
│  │   - Formatted HTML response                            │            │
│  │   - Citations with links                               │            │
│  │   - Response time                                      │            │
│  │   - Error messages (if any)                            │            │
│  └────────────────────────────────────────────────────────┘            │
│                                                                          │
│  ┌────────────────────────────────────────────────────────┐            │
│  │   Debug Area (Optional)                                │            │
│  │   - Agent reasoning steps                              │            │
│  │   - Retrieved chunks details                           │            │
│  │   - Scores and metadata                                │            │
│  │   - Full trace of execution                            │            │
│  └────────────────────────────────────────────────────────┘            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                      11. TESTING LAYER                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │
│  │  Test Suite  │  │  Smoke Tests │  │  Integration │  │  E2E Test  │ │
│  │  (8 tests)   │  │              │  │   Tests      │  │            │ │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤  ├────────────┤ │
│  │ • Loaders    │  │ • Quick pass │  │ • Components │  │ • Full     │ │
│  │ • Chunks     │  │ • <30s exec  │  │   working    │  │   workflow │ │
│  │ • VectorDB   │  │ • Critical   │  │   together   │  │ • Real     │ │
│  │ • Retrieve   │  │   paths      │  │              │  │   queries  │ │
│  │ • RAG        │  │              │  │              │  │            │ │
│  │ • LLM        │  │              │  │              │  │            │ │
│  │ • Agent      │  │              │  │              │  │            │ │
│  │ • Memory     │  │              │  │              │  │            │ │
│  └──────────────┘  └──────────────┘  └──────────────┘  └────────────┘ │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Flujo de Datos Detallado

### Flujo 1: Pregunta Legal (Con RAG)

```
Usuario escribe pregunta
       ↓
Agente ReAct recibe query
       ↓
Agente analiza: "¿Requiere documentos?" → SÍ
       ↓
Selecciona herramienta: BusquedaLegalRAG
       ↓
rag_answer(query) ejecuta:
  1. retrieve(query) → busca en vectordb
  2. Obtiene top-4 chunks más relevantes
  3. Construye contexto con chunks
  4. Crea prompt: "Responde basado en: [contexto]"
  5. llm_call(prompt) → genera respuesta
  6. Retorna {answer, citations}
       ↓
Agente formatea respuesta final
       ↓
UI muestra respuesta con referencias
```

### Flujo 2: Pregunta General (Sin RAG)

```
Usuario escribe pregunta
       ↓
Agente ReAct recibe query
       ↓
Agente analiza: "¿Requiere documentos?" → NO
       ↓
Selecciona herramienta: RespuestaDirecta
       ↓
llm_call(query) directo
       ↓
Agente formatea respuesta
       ↓
UI muestra respuesta (sin citas)
```

### Flujo 3: Carga de Documentos

```
Usuario sube PDF/TXT/URL
       ↓
Loader apropiado procesa:
  • PDF → PyPDF2
  • TXT → read()
  • URL → requests + BeautifulSoup
       ↓
Texto extraído
       ↓
RecursiveCharacterTextSplitter
       ↓
DOCUMENT_CHUNKS[] actualizado
       ↓
OpenAI Embeddings genera vectores
       ↓
Chroma indexa vectores
       ↓
Sistema listo para consultas
```

---

## 🔄 Ciclo de Vida de una Pregunta

```
1. INPUT      →  Usuario escribe en widget
2. ROUTE      →  Agente decide herramienta
3. RETRIEVE   →  Busca chunks (si RAG)
4. CONTEXT    →  Arma prompt con contexto
5. GENERATE   →  LLM produce respuesta
6. PARSE      →  Estructura output
7. CITE       →  Añade referencias
8. FORMAT     →  HTML para UI
9. DISPLAY    →  Muestra al usuario
10. MEMORY    →  Guarda en historial
```

---

## 🏗️ Componentes Clave

### Core Components

- **LLM Provider Factory**: Abstracción multi-proveedor
- **Vector Database**: Chroma con persistencia
- **RAG Pipeline**: retrieve → context → generate
- **ReAct Agent**: Razonamiento + herramientas
- **Memory System**: Contexto conversacional

### Support Components

- **Loaders**: PyPDF2, BeautifulSoup, TextLoader
- **Splitters**: RecursiveCharacterTextSplitter
- **Parsers**: StructuredOutputParser
- **UI**: ipywidgets con HTML formatting
- **Tests**: Suite automatizada de 8 tests

### Configuration

- **Environment Variables**: .env con multi-provider
- **Provider Classes**: OpenAI, Groq, OpenRouter, Ollama
- **Fallback Systems**: Keywords si falla vectordb

---

## 📈 Métricas de Performance

```
┌─────────────────────────────┬──────────────┐
│ Operación                   │ Tiempo       │
├─────────────────────────────┼──────────────┤
│ Carga de 1 PDF (100 págs)  │ ~2-3 s       │
│ Creación de chunks          │ <1 s         │
│ Generación de embeddings    │ 1-2 min*     │
│ Indexación en Chroma        │ 5-10 s       │
│ Búsqueda vectorial (k=4)    │ <1 s         │
│ Generación de respuesta     │ 3-8 s        │
│ Total por consulta (RAG)    │ 5-10 s       │
│ Total por consulta (Direct) │ 3-5 s        │
└─────────────────────────────┴──────────────┘

* Solo en primera indexación, luego reutiliza
```

---

## 🔐 Flujo de Seguridad

```
Variables de Entorno (.env)
       ↓
NO commitear al repo (.gitignore)
       ↓
Cargar con python-dotenv
       ↓
Pasar solo API keys necesarias
       ↓
Usar en providers encapsulados
       ↓
Nunca exponer en UI o logs
```

---

## 🎯 Puntos de Extensión

Fácilmente extensible en:

- **Nuevos Loaders**: Agregar Word, HTML, etc.
- **Nuevos LLMs**: Añadir Anthropic, Cohere, etc.
- **Nuevas Herramientas**: Ampliar agente con más tools
- **Otros Vector DBs**: FAISS, Pinecone, Weaviate
- **UI Mejorada**: Streamlit, Gradio, web app

---

_Arquitectura diseñada para ser modular, escalable y mantenible._
