# 💬 Preguntas Preparadas para la Demo

**Copia y pega estas preguntas durante la demostración**

---

## 📚 Categoría 1: Preguntas Legales (Usan RAG)

### Pregunta 1A - Libertad de Expresión

```
¿Qué artículo de la Constitución Colombiana protege la libertad de expresión?
```

**Respuesta esperada:** Artículo 20  
**Tiempo aprox:** 10-15 segundos  
**Modo:** Agente → BusquedaLegalRAG

---

### Pregunta 1B - Habeas Corpus (Documentos)

```
Resume brevemente el concepto de habeas corpus según los documentos cargados.
```

**Respuesta esperada:** Información del artículo 30 sobre habeas corpus  
**Tiempo aprox:** 15-20 segundos  
**Modo:** Agente → BusquedaLegalRAG

---

### Pregunta 1C - Deberes Estudiantiles

```
¿Cuáles son los principales deberes del estudiante según el reglamento académico?
```

**Respuesta esperada:** Listado de deberes del reglamento  
**Tiempo aprox:** 15-20 segundos  
**Modo:** Agente → BusquedaLegalRAG

---

### Pregunta 1D - Derechos Fundamentales

```
¿Qué dice la Constitución sobre el derecho a la educación?
```

**Respuesta esperada:** Información del artículo 67  
**Tiempo aprox:** 15-20 segundos  
**Modo:** Agente → BusquedaLegalRAG

---

## 💡 Categoría 2: Preguntas Generales (Usan LLM)

### Pregunta 2A - Habeas Corpus (Concepto)

```
Explica brevemente qué es el habeas corpus en términos generales.
```

**Respuesta esperada:** Definición conceptual sin documentos  
**Tiempo aprox:** 10-15 segundos  
**Modo:** Agente → RespuestaDirecta

---

### Pregunta 2B - Cultura General

```
¿Quién fue Gabriel García Márquez?
```

**Respuesta esperada:** Biografía breve del autor  
**Tiempo aprox:** 10-15 segundos  
**Modo:** Agente → RespuestaDirecta

---

### Pregunta 2C - Concepto Jurídico

```
Define qué es un sistema jurídico.
```

**Respuesta esperada:** Definición general  
**Tiempo aprox:** 10-15 segundos  
**Modo:** Agente → RespuestaDirecta

---

### Pregunta 2D - Estado de Derecho

```
Explica el concepto de estado de derecho.
```

**Respuesta esperada:** Explicación conceptual  
**Tiempo aprox:** 10-15 segundos  
**Modo:** Agente → RespuestaDirecta

---

## 🎯 Categoría 3: Preguntas Complejas (Opcional)

### Pregunta 3A - Comparación

```
¿Cuál es la diferencia entre habeas corpus y habeas data según los documentos?
```

**Respuesta esperada:** Explicación de ambos conceptos  
**Tiempo aprox:** 20-25 segundos  
**Modo:** Agente → BusquedaLegalRAG

---

### Pregunta 3B - Procedimientos

```
¿Qué procedimientos debe seguir un estudiante para solicitar un recurso de reposición?
```

**Respuesta esperada:** Información del reglamento sobre procedimientos  
**Tiempo aprox:** 20-25 segundos  
**Modo:** Agente → BusquedaLegalRAG

---

## 🔍 Para Modo Debug (Mostrar Razonamiento)

Usa estas con el checkbox de debug activado:

### Debug 1 - Ver Decisión del Agente

```
¿Qué es la libertad de expresión?
```

**Propósito:** Mostrar cómo el agente decide entre RAG y LLM  
**Observar:** El razonamiento paso a paso del agente

---

### Debug 2 - Ver Retrieval

```
Busca información sobre derechos fundamentales
```

**Propósito:** Mostrar los chunks recuperados y sus scores  
**Observar:** Los 4 documentos más relevantes y sus scores

---

## 🚫 Preguntas a EVITAR

### ❌ NO usar estas en la demo:

1. **Demasiado específicas:**

   ```
   ¿Qué dice el parágrafo 3 del artículo 123 literal b?
   ```

   _Razón:_ Muy técnico, puede no estar en los docs

2. **Ambiguas:**

   ```
   Cuéntame sobre leyes
   ```

   _Razón:_ Respuesta demasiado amplia

3. **Fuera del dominio:**

   ```
   ¿Cuál es la capital de Francia?
   ```

   _Razón:_ No demuestra capacidad legal

4. **Muy largas:**
   ```
   Dame un análisis completo y detallado de todos los artículos relacionados con...
   ```
   _Razón:_ Toma mucho tiempo

---

## 🎬 Secuencia Recomendada para Demo de 2 Minutos

### Opción A - Demo Estándar

1. **[10s]** Mostrar UI y explicar modos
2. **[30s]** Pregunta 1A (libertad de expresión)
3. **[20s]** Explicar respuesta y citas
4. **[20s]** Pregunta 2A (habeas corpus general)
5. **[15s]** Activar debug y hacer pregunta corta
6. **[15s]** Scroll a tests (mostrar 8/8 pass)

**Total: ~110 segundos = 1:50 minutos**

---

### Opción B - Demo con Énfasis en Agente

1. **[10s]** Mostrar UI
2. **[25s]** Pregunta 1A con debug activado
3. **[15s]** Señalar razonamiento del agente
4. **[25s]** Pregunta 2B sin documentos
5. **[15s]** Comparar decisiones del agente
6. **[10s]** Mostrar estadísticas finales

**Total: ~100 segundos = 1:40 minutos**

---

### Opción C - Demo Completa (Si tienes tiempo)

1. **[10s]** Mostrar UI y stats
2. **[30s]** Pregunta 1A (legal con RAG)
3. **[15s]** Explicar citas y trazabilidad
4. **[20s]** Pregunta 2A (general sin docs)
5. **[15s]** Cambiar a modo "Solo RAG"
6. **[20s]** Hacer pregunta 1C
7. **[15s]** Activar debug, pregunta corta
8. **[15s]** Mostrar tests

**Total: ~140 segundos = 2:20 minutos**

---

## 📝 Script de Narración

### Para Pregunta Legal (con RAG)

```
"Ahora hagamos una consulta que requiere buscar en los documentos:
[ESCRIBIR/PEGAR PREGUNTA]

Como pueden ver, el agente ReAct:
1. Analizó la pregunta
2. Decidió usar la herramienta de búsqueda legal
3. Recuperó los fragmentos más relevantes
4. Generó una respuesta basada en los documentos
5. Incluyó referencias exactas: [SEÑALAR CITAS]

Esto es clave - no son invenciones del modelo,
son citas verificables de los documentos reales."
```

---

### Para Pregunta General (sin RAG)

```
"Ahora una pregunta conceptual que NO requiere documentos:
[ESCRIBIR/PEGAR PREGUNTA]

Aquí el agente inteligentemente reconoció que es
una pregunta general y usó el LLM directamente,
sin perder tiempo buscando en los documentos.

Esta decisión automática es lo que hace al sistema eficiente."
```

---

### Para Modo Debug

```
"Si activamos el modo debug [ACTIVAR CHECKBOX],
podemos ver el razonamiento interno del agente:

[HACER PREGUNTA CORTA]

Como ven aquí [SEÑALAR ÁREA DEBUG]:
- El agente piensa paso a paso
- Decide qué herramienta usar
- Ejecuta la acción
- Devuelve el resultado

Esto nos da transparencia total del proceso."
```

---

## 💡 Tips de Presentación

### Al Hacer Preguntas:

1. **Lee la pregunta en voz alta** mientras la escribes
2. **Mantén las preguntas en pantalla** (no las borres rápido)
3. **Señala con el mouse** elementos clave de la respuesta
4. **Da tiempo** (2-3 segundos) para que vean la respuesta

### Al Mostrar Respuestas:

1. **Resalta las referencias/citas**
2. **Menciona el tiempo de respuesta** si es rápido
3. **Señala la estructura** (answer, citations, etc.)
4. **Compara** decisiones del agente entre preguntas

---

## 🎯 Objetivo de Cada Pregunta

| Pregunta                | Demuestra                       |
| ----------------------- | ------------------------------- |
| 1A (libertad expresión) | RAG funcional + citas           |
| 2A (habeas corpus)      | Decisión inteligente del agente |
| Debug activado          | Transparencia y razonamiento    |
| Tests                   | Calidad y cobertura             |

---

## 📊 Estadísticas para Mencionar

Mientras esperas respuesta, menciona:

- "El sistema tiene **1000+ chunks** indexados"
- "Soporta **4 proveedores** de LLM diferentes"
- "Pasó **8 de 8 tests** automatizados"
- "Busca en **2 documentos** legales colombianos"

---

## ✅ Checklist Antes de Cada Pregunta

- [ ] UI visible en pantalla
- [ ] Modo correcto seleccionado (Agent/RAG/LLM)
- [ ] Área de output limpia (o con respuesta anterior)
- [ ] Pregunta copiada y lista para pegar
- [ ] Sabes qué señalar en la respuesta

---

**¡Listo para impresionar! 🌟**

_Recuerda: La confianza al presentar es tan importante como el código._
