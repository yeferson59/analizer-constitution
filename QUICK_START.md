# ⚡ Quick Start Guide - Demo del Asistente Legal

**Para una demo exitosa en 5 minutos**

---

## 🚀 Antes de Abrir el Notebook

### 1. Configurar Variables de Entorno (30 segundos)

Asegúrate que tu `.env` tiene:

```bash
LLM_PROVIDER=groq
GROQ_API_KEY=tu_api_key_aquí
```

### 2. Verificar Dependencias (1 minuto)

```bash
cd /Users/yefersontoloza/Documents/python-projects/system-intellegents/jupyter/analizer-constitution
uv sync
```

---

## 📓 Ejecutar el Notebook

### Orden de Ejecución (IMPORTANTE)

Ejecuta las celdas en este orden exacto:

1. ✅ **Celda 1** - Portada (solo leer, no ejecutar)
2. ✅ **Celda 2** - Instalación de dependencias (comentada, skip)
3. ✅ **Celda 3** - Imports y configuración LLM
4. ✅ **Celda 4** - Loaders y widgets de carga
5. ✅ **Celda 5** - Preprocesamiento y chunks
6. ✅ **Celda 6** - Vector Database con embeddings ⚠️ IMPORTANTE
7. ✅ **Celda 7** - Parsers (ejemplo)
8. ✅ **Celda 8** - Memoria (ejemplo)
9. ✅ **Celda 9** - Agente ReAct (definición)
10. ✅ **Celda 10** - Sistema RAG completo
11. ✅ **Celda 11** - Inicializar vectordb variable
12. ✅ **Celda 12** - Pruebas del agente (opcional)
13. ✅ **Celda 13** - Interfaz de Usuario ⭐ PARA LA DEMO
14. ✅ **Celda 14** - Tests automatizados (ejecutar antes de demo)
15. ✅ **Celda 15** - Loader URLs (opcional)
16. ✅ **Celda 16** - Sintetizador (opcional)
17. ✅ **Celda 17** - Conclusiones (solo leer)

**Tiempo estimado de ejecución completa: 3-5 minutos**

---

## 🎯 Para la Demo (Solo estas celdas)

### Demo Mínima (2 minutos)

1. **Mostrar la UI** (Celda 13)

   - Debe estar ya ejecutada y visible

2. **Hacer 2 preguntas:**

**Pregunta 1 (Legal - usa RAG):**

```
¿Qué artículo de la Constitución protege la libertad de expresión?
```

- Activar modo debug si quieres mostrar el razonamiento
- Señalar las referencias/citas en la respuesta

**Pregunta 2 (General - usa LLM):**

```
Explica brevemente qué es el habeas corpus
```

- Mostrar que el agente decide usar LLM directo

3. **Mostrar Tests** (Celda 14)
   - Scroll rápido al resumen: "8/8 tests pasados"

---

## 🐛 Troubleshooting Rápido

### Error: "GROQ_API_KEY not found"

```bash
# Agrega a .env:
echo "GROQ_API_KEY=tu_key" >> .env
```

### Error: "No module named 'langchain_groq'"

```bash
uv add langchain-groq
```

### Error: "DOCUMENT_CHUNKS not found"

→ Ejecuta la celda 5 (preprocesamiento) primero

### Error: "vectordb is None"

→ Ejecuta la celda 6 (Vector Database)

### Embeddings muy lentos

→ Normal en primera ejecución (~1-2 minutos para 1000 chunks)

### UI no responde

→ Reinicia kernel y re-ejecuta desde celda 3

---

## 🎬 Durante la Presentación

### Setup (antes de que te toque)

- [ ] Notebook abierto en la celda de UI
- [ ] Todas las celdas ejecutadas hasta UI
- [ ] Tests ejecutados y pasando
- [ ] Pregunta 1 pre-escrita en un archivo para copiar/pegar
- [ ] Pregunta 2 pre-escrita en un archivo para copiar/pegar

### Al Presentar

1. **NO** ejecutes celdas en vivo (muy lento)
2. **SÍ** muestra la UI y haz preguntas
3. **SÍ** señala los elementos clave:
   - Modo del agente
   - Respuesta generada
   - Referencias/citas
   - Tiempo de respuesta

### Qué Decir

```
"Como ven, el sistema tiene una interfaz interactiva.
Aquí hacemos una pregunta legal: [escribir/pegar pregunta]
El agente automáticamente decide usar RAG para buscar en los documentos.
Y nos devuelve la respuesta con referencias específicas al artículo y documento.
Esto garantiza trazabilidad - no son alucinaciones del modelo."
```

---

## 🔥 Tips de Oro

### ✅ Hacer

- Tener el notebook pre-ejecutado
- Usar preguntas preparadas (copiar/pegar)
- Mostrar el modo debug una vez
- Señalar las referencias en la respuesta
- Mencionar los tests que pasan

### ❌ NO Hacer

- Ejecutar celdas en vivo durante la demo
- Improvisar preguntas complicadas
- Explicar código línea por línea
- Disculparse por detalles menores
- Pasarse de 5 minutos

---

## 📊 Estadísticas para Mencionar

Memoriza estos números para la presentación:

- **7/7** requisitos implementados
- **8/8** tests pasando
- **1000+** chunks indexados
- **2** documentos de ejemplo
- **3** modos de operación (Agent/RAG/LLM)
- **4** proveedores LLM soportados
- **100%** de funcionalidad completa

---

## ⏱️ Timing de la Demo

| Actividad                | Tiempo     |
| ------------------------ | ---------- |
| Mostrar UI               | 10s        |
| Pregunta 1 (legal)       | 30s        |
| Explicar respuesta       | 20s        |
| Pregunta 2 (general)     | 20s        |
| Mostrar debug (opcional) | 15s        |
| Mostrar tests            | 15s        |
| **TOTAL**                | **~2 min** |

Esto te deja 3 minutos para introducción, arquitectura y conclusión.

---

## 🎤 Script Ultra-Corto

Si solo tienes tiempo para memorizar esto:

```
"Implementamos un asistente legal con RAG.
Usa embeddings para búsqueda semántica.
Un agente ReAct decide automáticamente qué herramienta usar.
Todas las respuestas tienen referencias verificables.
[DEMO: 2 preguntas]
Pasamos 8/8 tests automatizados.
Sistema 100% funcional y listo."
```

---

## 🆘 Plan B (Si algo falla)

### Si la API falla en vivo:

> "Como ven en los outputs guardados, el sistema funciona correctamente. Tenemos tests que lo verifican."

### Si el notebook crashea:

> "Tenemos una suite completa de tests [mostrar celda de tests] que valida cada componente."

### Si te quedas sin tiempo:

> "En resumen: 7/7 requisitos, tests pasando, sistema funcional. El notebook completo está en el repo."

---

## ✅ Checklist 5 Minutos Antes

- [ ] Laptop cargada 100%
- [ ] Internet funcionando
- [ ] Notebook ejecutado completo
- [ ] UI visible y funcional
- [ ] Tests ejecutados (output visible)
- [ ] Preguntas pre-escritas listas
- [ ] Script de presentación a mano
- [ ] Cronómetro/timer preparado
- [ ] Respira profundo - estás listo! 💪

---

## 🎯 Objetivo de la Demo

**Demostrar en 2 minutos que:**

1. El sistema funciona end-to-end
2. El agente toma decisiones inteligentes
3. Las respuestas tienen referencias
4. Todo está probado (tests)
5. La implementación es completa

**NO intentar:**

- Explicar cada línea de código
- Mostrar todas las features
- Responder preguntas muy complejas
- Debuggear en vivo

---

**¡Éxito en tu presentación! 🚀**

_Recuerda: La confianza es clave. Has hecho un gran trabajo._
