**Python Testaufgabe**

Hallo! Nehmen Sie sich gerne Zeit, diese kurze Aufgabe zu erledigen, um uns zu zeigen, dass Sie wirklich an einer Zusammenarbeit mit uns interessiert sind. Teilen Sie Ihr Ergebnis mit Viktoria über Tg.

*   **Fristen:** 2 Arbeitstage ab dem Zeitpunkt des Erhalts der Testaufgabe.

**Was zu bauen ist**

1.  Ein LangGraph zustandsloser Chat-Graph — der Bot antwortet auf jede Benutzernachricht.
2.  Ein Agent, der das Tool `get_current_time` verwendet, das das LLM aufruft, wenn der Benutzer nach der Uhrzeit fragt. Z.B.:

    ```python
    def get_current_time() -> dict:
        """Gibt die aktuelle UTC-Zeit im ISO-8601-Format zurück.
        Beispiel -> {"utc": "2025-05-21T06:42:00Z"}"""
    ```

3.  Starten mit `langgraph dev`. Stellen Sie sicher, dass Ihre Projektstruktur dies unterstützt.
4.  Minimales Repository — eine einzelne Python-Datei, `requirements.txt` und eine kurze README.

**Einschränkungen**

*   Jedes Modell ist in Ordnung (GPT, Gemini, DeepSeek, Ollama mit lokalen Modellen, ...).
*   Wenn Sie auf Ollama oder andere lokale Runner angewiesen sind, fügen Sie genaue Setup-Befehle (`ollama pull ...`, Standardport usw.) hinzu.
*   Kein Speicher oder Datenbanken. Genau ein Tool (`get_current_time`).
*   Strenges Zeitlimit: bis zu 90 Minuten — pushen Sie, was auch immer läuft.

**Wie wir es ausführen werden**

```bash
git clone <your_repo>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
langgraph dev
```

Wenn während einer mehrteiligen Konversation die Frage "Wie spät ist es?" das Tool auslöst und die korrekte Zeit zurückgibt, haben Sie bestanden 😉 und wir können zum nächsten Teil (Interview) übergehen.