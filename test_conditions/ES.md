**Tarea de prueba de Python**

¡Hola! Siéntase libre de completar esta corta tarea para asegurarnos de que está realmente interesado en trabajar con nosotros. Comparta su resultado con Viktoria vía Tg.

*   **Plazos:** 2 días hábiles a partir del momento de recibir la tarea de prueba.

**Qué construir**

1.  Un grafo de chat sin estado de LangGraph — el bot responde a cada mensaje del usuario.
2.  Un agente que use la herramienta `get_current_time` que el LLM llamará cuando el usuario pregunte la hora. Ej:

    ```python
    def get_current_time() -> dict:
        """Devuelve la hora UTC actual en formato ISO-8601.
        Ejemplo -> {"utc": "2025-05-21T06:42:00Z"}"""
    ```

3.  Lanzar con `langgraph dev`. Asegúrese de que la estructura de su proyecto lo soporte.
4.  Repositorio mínimo — un solo archivo Python, `requirements.txt`, y un README corto.

**Restricciones**

*   Cualquier modelo es válido (GPT, Gemini, DeepSeek, Ollama con modelos locales, ...).
*   Si depende de Ollama u otros ejecutores locales, incluya los comandos de configuración exactos (`ollama pull ...`, puerto predeterminado, etc.).
*   Sin memoria ni bases de datos. Exactamente una herramienta (`get_current_time`).
*   Límite de tiempo estricto: hasta 90 minutos — suba lo que funcione.

**Cómo lo ejecutaremos**

```bash
git clone <your_repo>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
langgraph dev
```

Si durante la conversación multiturno la pregunta "¿Qué hora es?" activa la herramienta y devuelve la hora correcta, usted aprueba 😉 y podemos proceder a la siguiente parte (entrevista).