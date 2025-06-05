**Tâche de test Python**

Bonjour ! N'hésitez pas à compléter cette courte tâche pour nous assurer que vous êtes réellement intéressé(e) à travailler avec nous. Partagez votre résultat avec Viktoria via Tg.

*   **Délais :** 2 jours ouvrables à compter de la réception de la tâche de test.

**Ce qu'il faut construire**

1.  Un graphe de chat sans état LangGraph — le bot répond à chaque message utilisateur.
2.  Un agent utilisant l'outil `get_current_time` que le LLM appelle lorsque l'utilisateur demande l'heure. Ex:

    ```python
    def get_current_time() -> dict:
        """Renvoie l'heure UTC actuelle au format ISO-8601.
        Exemple -> {"utc": "2025-05-21T06:42:00Z"}"""
    ```

3.  Lancement avec `langgraph dev`. Assurez-vous que la structure de votre projet le supporte.
4.  Dépôt minimal — un seul fichier Python, `requirements.txt`, et un court README.

**Contraintes**

*   Tout modèle convient (GPT, Gemini, DeepSeek, Ollama avec des modèles locaux, ...).
*   Si vous dépendez d'Ollama ou d'autres exécuteurs locaux, incluez les commandes de configuration exactes (`ollama pull ...`, port par défaut, etc.).
*   Pas de mémoire ni de bases de données. Exactement un seul outil (`get_current_time`).
*   Temps imparti strict : jusqu'à 90 minutes — poussez ce qui fonctionne.

**Comment nous allons l'exécuter**

```bash
git clone <your_repo>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
langgraph dev
```

Si, lors d'une conversation à plusieurs tours, la question "Quelle heure est-il ?" déclenche l'outil et renvoie l'heure correcte, vous passez 😉 et nous pourrons passer à la partie suivante (entretien).