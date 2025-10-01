# 🎤 Script de Presentación - 5 Minutos

**Proyecto:** Asistente Legal Colombiano con LangChain + LLM  
**Tiempo Total:** 5 minutos  
**Fecha:** 2 de octubre de 2025

---

## 📋 Preparación Pre-Presentación

### Checklist antes de comenzar:

- [ ] Notebook ejecutado completamente (sin errores)
- [ ] Vector database creado y funcional
- [ ] Widgets de UI funcionando
- [ ] Tests pasados exitosamente
- [ ] Documento de ejemplo cargado
- [ ] Variables de entorno configuradas

### Estado del sistema a verificar:

```
✅ Documentos cargados: 2
✅ Chunks generados: 400+
✅ Vector DB: Activo
✅ Agente ReAct: Inicializado
✅ UI: Funcional
```

---

## 🎬 Estructura de la Presentación

### [0:00 - 0:30] Introducción (30 segundos)

**Persona 1:**

> "Buenos días/tardes. Somos [nombres del equipo] y les presentamos nuestro **Asistente Legal Colombiano Inteligente**.
>
> Este sistema permite consultar la Constitución Política de Colombia y documentos normativos usando **Inteligencia Artificial**, específicamente **RAG (Retrieval-Augmented Generation)** y **agentes ReAct** de LangChain.
>
> El objetivo es facilitar el acceso a información legal de forma rápida y precisa, con referencias verificables."

---

### [0:30 - 1:30] Arquitectura (1 minuto)

**Persona 2:**

> "La arquitectura del sistema integra **todos los componentes vistos en clase**:
>
> **1. Loaders** - Cargamos PDFs, archivos de texto e incluso URLs de documentos legales
>
> **2. Transformadores** - Dividimos los documentos en chunks de 1000 caracteres con overlap
>
> **3. Embeddings y Vector DB** - Usamos OpenAI Embeddings con Chroma para búsqueda semántica
>
> **4. RAG Pipeline** - Recuperamos los fragmentos más relevantes y los enviamos al LLM junto con la pregunta
>
> **5. Memoria** - Mantenemos contexto entre preguntas con ConversationBufferMemory
>
> **6. Agentes ReAct** - Un agente decide automáticamente si usar RAG para documentos o el LLM directo para preguntas generales
>
> **7. Parsers** - Estructuramos las respuestas con JSON schema validado"

**[MOSTRAR DIAGRAMA EN PANTALLA SI ESTÁ DISPONIBLE]**

---

### [1:30 - 3:30] Demo en Vivo (2 minutos) ⭐

**Persona 3:**

> "Ahora veamos el sistema en acción. Aquí tenemos nuestra **interfaz interactiva** creada con Jupyter widgets."

#### Demo Paso 1: Pregunta Legal (45 segundos)

**[SCROLL A LA UI]**

> "Primero, una pregunta que **requiere buscar en los documentos**:"

**Escribir en el widget:**

```
¿Qué artículo de la Constitución protege la libertad de expresión?
```

**[CLICK EN "CONSULTAR"]**

> "Como ven, el sistema:
>
> 1. Activó automáticamente el agente ReAct
> 2. El agente decidió usar la herramienta de búsqueda RAG
> 3. Recuperó los fragmentos relevantes de la Constitución
> 4. Generó una respuesta citando el **Artículo 20**
> 5. Y nos muestra las **referencias exactas** con el documento y chunk"

**[SEÑALAR LAS CITAS EN PANTALLA]**

#### Demo Paso 2: Pregunta General (30 segundos)

> "Ahora una pregunta que NO requiere documentos:"

**Escribir:**

```
Explica brevemente qué es el habeas corpus en términos generales
```

**[CLICK EN "CONSULTAR"]**

> "Aquí el agente inteligentemente eligió usar el LLM directo, sin buscar en documentos, porque es una pregunta conceptual general."

#### Demo Paso 3: Funcionalidades Extra (45 segundos)

**[ACTIVAR CHECKBOX DE DEBUG]**

> "Si activamos el **modo debug**, podemos ver el razonamiento interno del agente paso a paso."

**[HACER UNA CONSULTA RÁPIDA]**

**[SCROLL A TESTS]**

> "También implementamos **tests automatizados** que verifican cada componente:"

**[MOSTRAR OUTPUT DE TESTS - debe mostrar PASS]**

> "Como ven, todos los tests pasan: loaders ✓, chunks ✓, vector DB ✓, RAG ✓, agente ✓"

---

### [3:30 - 4:30] Punto Destacado (1 minuto)

**Persona 1:**

> "Lo más valioso de este proyecto es la **trazabilidad y verificabilidad**.
>
> A diferencia de un ChatGPT normal que puede 'alucinar' información, nuestro sistema:
>
> **1. Solo responde basándose en documentos reales**  
> **2. Cita exactamente de dónde sacó cada información**  
> **3. Permite verificar las fuentes originales**
>
> Esto es crítico en el ámbito legal donde la precisión es fundamental.
>
> Además, implementamos **soporte multi-proveedor** - funciona con OpenAI, Groq, Ollama u OpenRouter - lo que da flexibilidad según el presupuesto y necesidades.
>
> Y el **agente ReAct** hace el sistema más inteligente - decide automáticamente la mejor estrategia para cada pregunta."

---

### [4:30 - 5:00] Limitaciones y Cierre (30 segundos)

**Persona 2:**

> "Finalmente, es importante mencionar las **limitaciones**:
>
> - ⚠️ **NO reemplaza a un abogado** - es una herramienta de consulta educativa
> - Los documentos deben actualizarse manualmente
> - La calidad depende de los documentos cargados
> - Siempre se debe verificar con fuentes oficiales
>
> **En resumen:** Implementamos exitosamente los 7 puntos del enunciado: mensajes, parsers, loaders, vector DB, RAG, memoria y agentes.
>
> El sistema está **funcional, documentado y listo para uso educativo**.
>
> ¿Preguntas?"

**[FIN - EXACTAMENTE A LOS 5 MINUTOS]**

---

## 🎯 Distribución de Tiempos (Resumen)

| Sección             | Tiempo   | Responsable |
| ------------------- | -------- | ----------- |
| Introducción        | 0:30     | Persona 1   |
| Arquitectura        | 1:00     | Persona 2   |
| Demo en Vivo        | 2:00     | Persona 3   |
| Punto Destacado     | 1:00     | Persona 1   |
| Limitaciones/Cierre | 0:30     | Persona 2   |
| **TOTAL**           | **5:00** | -           |

---

## 💡 Tips para la Presentación

### Para el Presentador:

1. **Practica 2-3 veces** antes del día real
2. **Cronometra cada sección** - usa un timer visible
3. **Ten el notebook ya ejecutado** - no ejecutes en vivo (solo muestra)
4. **Prepara las preguntas pre-escritas** en un archivo aparte para copiar/pegar rápido
5. **Ten backup del output** por si algo falla en vivo

### Cosas que NO hacer:

❌ Ejecutar celdas que tardan mucho  
❌ Explicar código línea por línea  
❌ Pasarse de 5 minutos (es descalificante)  
❌ Improvisar - sigue el script  
❌ Disculparse por errores menores

### Qué enfatizar:

✅ **Integración completa** de todos los componentes  
✅ **Trazabilidad** de las respuestas  
✅ **Inteligencia del agente** ReAct  
✅ **Tests** que demuestran calidad  
✅ **Consideraciones éticas** y limitaciones

---

## 🎬 Frases Clave a Memorizar

**Para impresionar:**

1. "Implementa RAG para eliminar alucinaciones del LLM"
2. "El agente ReAct decide inteligentemente qué herramienta usar"
3. "Cada respuesta incluye referencias verificables"
4. "Tests automatizados garantizan la calidad del sistema"
5. "Soporte multi-proveedor para flexibilidad"

---

## 📱 Plan B (Si algo falla)

### Si la API del LLM falla:

> "Como pueden ver en el código, el sistema maneja errores y usa fallback por keywords"

### Si el notebook tiene un error:

> "Tenemos tests que verifican cada componente individualmente [mostrar tests]"

### Si se acaba el tiempo:

> "En resumen: sistema funcional, documentado, con todos los requisitos implementados"

---

## 🏁 Checklist Final Día de Presentación

**30 minutos antes:**

- [ ] Laptop cargada al 100%
- [ ] Notebook abierto y ejecutado completamente
- [ ] Verificar que todos los widgets funcionan
- [ ] Internet estable (para API del LLM)
- [ ] Script impreso o en segunda pantalla
- [ ] Timer/cronómetro listo

**5 minutos antes:**

- [ ] Respira profundo
- [ ] Revisa el script mentalmente
- [ ] Verifica que la UI esté visible
- [ ] Ten confianza - preparaste bien el proyecto

---

## 🎓 Posibles Preguntas del Profesor

**P: "¿Por qué usaron Chroma en lugar de FAISS?"**  
R: "Chroma ofrece persistencia automática y es más fácil de integrar, pero el sistema soporta ambos."

**P: "¿Cómo manejan la actualización de documentos?"**  
R: "Actualmente es manual, pero hay un loader de URLs y el vector DB se puede regenerar fácilmente."

**P: "¿Qué pasa si el agente se equivoca?"**  
R: "El sistema siempre muestra las fuentes, permitiendo verificación manual. Además el modo debug muestra el razonamiento."

**P: "¿Qué tan escalable es?"**  
R: "Con Chroma y embeddings, es muy escalable. Probado con 400+ chunks sin problemas de performance."

---

**¡Buena suerte en la presentación! 🍀**

Recuerda: Has hecho un excelente trabajo. Solo muestra lo que construiste con confianza.
