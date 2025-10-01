# Roadmap detallado — Asistente legal / normativo (LangChain + LLMs)

## Estado Actual del Proyecto (Actualizado)

El proyecto ha sido mejorado con soporte para múltiples proveedores de LLM:

### Arquitectura Multi-Proveedor
- **Módulo `llm_providers.py`**: Implementación de clases para soporte de múltiples proveedores
  - `OpenAIProvider`: Soporte para modelos de OpenAI (GPT-3.5, GPT-4, etc.)
  - `OpenRouterProvider`: Soporte para OpenRouter (compatible con API de OpenAI)
  - `OllamaProvider`: Soporte para modelos locales con Ollama
  - `GroqProvider`: Soporte para modelos de Groq (Llama, Mixtral, etc.)
  - `LLMProviderFactory`: Factory pattern para crear proveedores fácilmente
  - Función `get_llm_client()`: Interfaz unificada para obtener cliente LLM

### Mejoras Realizadas
- ✅ Limpieza de código: eliminación de código comentado y duplicado
- ✅ Arquitectura basada en clases para extensibilidad
- ✅ Configuración mediante variables de entorno
- ✅ Documentación actualizada
- ✅ Soporte para múltiples proveedores sin cambiar el código del notebook

### Configuración
Ver `.env.example` para configurar las variables de entorno necesarias:
- `LLM_PROVIDER`: Selecciona el proveedor (openai, openrouter, ollama, groq)
- Variables específicas por proveedor para API keys y modelos

---

Fecha del objetivo: Jueves 2 de octubre (presentación de 5 minutos)

Resumen rápido
- Objetivo: Desarrollar en un Jupyter Notebook un chatbot asistente legal para consultar leyes colombianas que integre todas las herramientas vistas en clase (mensajes/plantillas, parsers, loaders, vector DB + RAG, memoria LangChain, agentes ReAct, transformaciones de documentos). Usar únicamente LangChain (no LangGraph).
- Entrega: Notebook Jupyter único bien documentado, con widgets interactivos y sección de demo. La presentación debe durar 5 minutos; un integrante (aleatorio) realizará la exposición.

Suposiciones razonables
- Tendrán claves de API en variables de entorno (p. ej. `OPENAI_API_KEY`, `OPENAI_BASE_URL` o la que corresponda al LLM usado).
- Se usarán librerías ya vistas en clase (LangChain, ipywidgets, una vector DB ligera como FAISS/Chroma integrable con LangChain).
- Los documentos legales disponibles serán archivos locales (.pdf, .txt, .md) y/o URLs públicas. Si hace falta, incluir un pequeño set de ejemplo en la carpeta `data/`.

Contrato mínimo (inputs / outputs / criterios)
- Input: consultas de usuario vía widget (pregunta en lenguaje natural) y/o archivos legales subidos.
- Output: respuesta textual con referencias (párrafo/fragmento fuente) y trazabilidad (qué documento/offset fue usado). En modo debug, mostrar embeddings/score/ranking.
- Errores: manejar falta de documentos, clave de API faltante, consultas fuera de dominio.
- Criterio de éxito: notebook ejecutable de principio a fin en < 5 min de demo; cada punto (a–g) debe estar implementado y documentado.

Estructura del Notebook (secciones obligatorias)
1. Portada y objetivos
   - Título, autores, objetivo corto, resumen de la demo.
2. Instalación / imports / carga de variables de entorno
   - `!pip install` (si es necesario), `from langchain...`, `ipywidgets` y `dotenv`.
3. Preparación de datos (Loaders)
   - Subida local con `ipywidgets.FileUpload` y loaders para PDF/TXT/HTML.
   - Loader desde URL (requests + TextLoader/HTMLLoader de LangChain si se usó en clase).
   - Mostrar una celda que inspeccione y previsualice los documentos cargados.
4. Transformación de documentos
   - Splitters: dividir por párrafos/secciones (p. ej. `RecursiveCharacterTextSplitter`).
   - Compresores/sanitizadores: quitar ruido, normalizar caracteres, metadatos (título, fecha).
   - Sintetizadores: agregar una celda con función para generar resúmenes de un documento (llamada a LLM).
5. Parsers para formato de salida
   - Uso de parsers/validators para asegurar la estructura de salida (p. ej. JSON schema / output parser de LangChain).
   - Ejemplo: respuesta con campos {answer, citations:[{doc,score,chunk}], follow_up:bool}.
6. Embeddings y Vector DB (RAG)
   - Crear embeddings con la embedding API estudiada.
   - Indexar chunks en una vector DB (FAISS o Chroma) y mostrar cómo buscar k-NN.
   - Implementar pipeline RAG: recuperación → contexto → prompt → LLM.
7. Gestión de memoria
   - Implementar una clase de memoria de LangChain (ConversationBufferMemory o similar vista en clase).
   - Mostrar cómo persiste el contexto entre interacciones en el widget.
8. Uso de agentes ReAct
   - Configurar un agente ReAct que pueda decidir: buscar en vector DB, llamar al LLM, o ejecutar una acción externa (p. ej. abrir un documento o extraer una cláusula).
   - Incluir ejemplos de herramientas definidas y una ejecución controlada (límites de pasos).
9. Interfaz con Widgets
   - Widgets: Text box para pregunta, Botón "Enviar", Dropdown para seleccionar fuente (local/URL), FileUpload para documentos, Output para respuestas, controles para ver debug.
   - Un flujo de UI mínimo: cargar documentos → indexar → preguntar.
10. Pruebas y verificación (smoke tests)
   - Celdas que corran tests rápidos: loader funciona, embeddings generados, vector DB retorna matches, agente ejecuta 1–2 ejemplos.
11. Conclusión / discusión ética y limitaciones
   - Limitaciones de cobertura legal, necesidad de verificación humana, fuentes y actualización.

Checklist de requisitos del enunciado (mapa a secciones del notebook)
- a) Mensajes y plantillas — Sección: Prompt templates y ejemplo de mensajes multi-turn.
- b) Parsers para formato de salida — Sección: Parsers y JSON schema para respuestas.
- c) Loaders desde fuentes locales/externas — Sección: Preparación de datos (Loaders) + FileUpload + URL loader.
- d) Vector DB + RAG mediante embeddings — Sección: Embeddings & Vector DB.
- e) Gestión de memoria — Sección: Memoria LangChain (ConversationBufferMemory etc.).
- f) Agentes ReAct — Sección: Agente y herramientas.
- g) Transformación de documentos — Sección: Splitters / compresores / sintetizadores.

Tareas diarias (plan corto hasta la presentación)
Nota: hoy es 27-sep; disponen de 5 días incluyendo el día de la presentación. Ajusten según disponibilidad del grupo.

- Día 0 (27-sep): Planificación rápida y asignación de tareas
  - Leer el enunciado y definir rol para cada integrante (máx 3): 1) Data/Loaders, 2) RAG/Vector DB, 3) UI/Agente + documentación.
  - Crear repositorio/notebook base y añadir `ROADMAP.md` y carpeta `data/` con ejemplos: Constitución (extractos), decreto de ejemplo.

- Día 1 (28-sep): Loaders + transformación de documentos
  - Implementar loaders para PDF/TXT/URL.
  - Crear splitters y sanitizador de texto. Indexar localmente los documentos sin embeddings aún.
  - Entregable: notebook con celdas que carguen y dividan documentos correctamente.

- Día 2 (29-sep): Embeddings + Vector DB + RAG básico
  - Configurar embeddings y vector store (FAISS/Chroma). Indexar chunks.
  - Implementar retrieval + prompt template que incluya contexto recuperado.
  - Entregable: consulta RAG simple con output mostrado y citas.

- Día 3 (30-sep): Parsers, Memoria y Agente ReAct
  - Añadir output parser para respuestas (estructura JSON) y validación.
  - Integrar ConversationMemory para mantener contexto.
  - Implementar un agente ReAct simple con 2 herramientas: retriever y search_local (abrir doc/responder).
  - Entregable: agent workflow funcionando en 2 ejemplos.

- Día 4 (1-oct): Interfaz (widgets), documentación & pruebas
  - Construir widgets para la interacción y un panel de debug.
  - Añadir celdas que automaticen tests rápidos (smoke tests) y documentación paso a paso.
  - Entrenar/practicar la demo interna y ajustar tiempos.

- Día 5 (2-oct — día de presentación): Ensayo final y presentación
  - Revisión final del notebook y limpiar outputs innecesarios.
  - Hacer 2 ensayos de 5 minutos y preparar quién mostrará qué (ver script abajo).

Roles y asignación (grupo hasta 3 personas)
- Rol A — Data & Loaders (archivos, limpieza, splitters).
- Rol B — RAG & Vector DB (embeddings, indexado, retrieval).
- Rol C — UI & Agente (widgets, memoria, agente ReAct, documentación y presentación).

Actitudes recomendadas
- Mantener commits pequeños y descriptivos.
- Documentar cada celda con un encabezado y comentario de lo que hace.
- Usar variables de entorno para claves y no subirlas al repo.

Pruebas rápidas y quality gates antes de la entrega
- Build / Dependencias: verificar `pip install -r requirements.txt` (o celdas `!pip install`).
- Lint/Typecheck: revisar errores visibles y que el notebook corra de arriba a abajo.
- Tests unitarios mínimos (en notebook):
  - Loader smoke: cargar 3 documentos y comprobar número de chunks > 0.
  - Embedding smoke: crear embedding para 1 chunk y que devuelva vector de tamaño esperado.
  - Retriever smoke: buscar con query conocida y comprobar que la respuesta incluya citas con score.
  - Agent smoke: ejecutar una consulta que desencadene 1 acción y verificar resultado.

Edge cases a considerar
- Documentos muy largos → paginar o limitar chunks indexados.
- Ambigüedad en la pregunta → agente sugiere follow-up question.
- Sin conexión a API de LLM o límites de cuota → fallback: respuestas basadas solo en retrieval (mostrar cita literal y decir "No pude generar respuesta final por falta de API").

Recomendaciones técnicas concretas
- Vector DB: usar Chroma si quieren persistir fácilmente o FAISS para in-memory rápido.
- Embeddings: usar la implementación que vimos en clase (asegurar compatibilidad con LangChain).
- Parsers: usar LangChain OutputParsers o validación con jsonschema para estructurar respuestas.
- Agentes: limitar max_steps para evitar loops; usar herramientas explicitadas con docstrings.
- Widgets: `ipywidgets.Text`, `Button`, `Dropdown`, `FileUpload`, `Output`, y `VBox/HBox` para layout.

Script de presentación (5 minutos)
Distribuir tiempos y quién hablará (si son 3, cada uno 1:30 aprox.)

- 0:00–0:30 — Introducción (1 frase): título, integrantes, objetivo del proyecto.
- 0:30–1:30 — Arquitectura en 30s: explicar (rápidamente) los bloques: Loaders → Transformadores → Embeddings → Vector DB (RAG) → LLM + Memory → Agente + UI.
- 1:30–3:30 — Demo (2 min):
  - Mostrar notebook (sección de carga/indexado ya hecha).
  - Enviar una pregunta tipo: "¿Qué artículo de la Constitución protege la libertad de expresión?".
  - Enseñar la respuesta generada, resaltar las citas y el parser JSON (mostrar estructura con fields: answer, citations).
  - (Opcional) Mostrar agente ReAct haciendo una búsqueda y luego llamando al LLM para sintetizar.
- 3:30–4:30 — Lo más interesante (1 min): resaltar la parte que el grupo considere más valiosa — p. ej. la trazabilidad de RAG o el agente ReAct que decide acciones.
- 4:30–5:00 — Limitaciones y cierre: explicar limitaciones (fuentes, responsabilidad legal), seguir mejorando.

Materiales a entregar (en el repo)
- `main.ipynb` — Notebook completo, documentado y ejecutable.
- `data/` — Documentos de ejemplo (extractos legales) o scripts para descargar ejemplos.
- `requirements.txt` o celdas `!pip install ...` dentro del notebook.
- `ROADMAP.md` (este archivo) y `README.md` con instrucciones de ejecución rápida.

Checklist pre-entrega (quick)
- [x] Notebook ejecuta de arriba a abajo sin errores (salvo la falta de key que se documenta).
- [x] Todos los puntos (a–g) están implementados y señalados en el notebook.
- [x] Widgets funcionales para la demo.
- [ ] Ensayo de 5 minutos realizado al menos 2 veces.
- [x] Documentos ejemplo en `data/` y variables de entorno explicadas en `README.md`.
- [x] Soporte multi-proveedor (OpenAI, OpenRouter, Ollama, Groq) implementado.
- [x] Código limpio y sin duplicados/comentarios innecesarios.

Siguientes pasos inmediatos (qué hacer ahora)
1. Repartir roles y crear el notebook `main.ipynb`/branch de trabajo.
2. Añadir 2–3 documentos legales de ejemplo en `data/`.
3. Implementar loaders y splitter (día 1) y comprobar con tests rápidos.
4. Ir completando según plan y ensayar la demo el 1-oct.

Contacto y aportes
Si quieren, puedo ayudar a convertir este roadmap en una plantilla de notebook (celdas iniciales con headers y funciones vacías) para acelerar el arranque.

---

Fin del roadmap.
