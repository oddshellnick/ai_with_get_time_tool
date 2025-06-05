**Python Test Task**

Hey! Feel free to complete this short task to make us sure that you are really interested in working with us. Share your result with Viktoria via Tg.

*   **Deadlines:** 2 working days from the moment of receiving the test task.

**What to build**

1.  LangGraph stateless chat graph — the bot replies to each user message.
2.  Agent using tool `get_current_time` that the LLM calls when the user asks for the time. E.g:

    ```python
    def get_current_time() -> dict:
        """Return the current UTC time in ISO-8601 format.
        Example -> {"utc": "2025-05-21T06:42:00Z"}"""
    ```

3.  Launch with `langgraph dev`. Ensure your project structure supports this.
4.  Minimal repo — a single Python file, `requirements.txt`, and a short README.

**Constraints**

*   Any model is fine (GPT, Gemini, DeepSeek, Ollama with local models, ...).
*   If you depend on Ollama or other local runners, include exact setup commands (`ollama pull ...`, default port, etc.).
*   No memory or databases. Exactly one tool (`get_current_time`).
*   Hard time-box: up to 90 minutes — push whatever runs.

**How we'll run it**

```bash
git clone <your_repo>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
langgraph dev
```

If during multi-turn conversation asking "What time is it?" triggers the tool and returns the correct time, you pass 😉 and we can proceed to the next part (interview).