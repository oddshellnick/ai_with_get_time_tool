# ai_with_get_time_tool: A ReAct agent with LangChain, Ollama, and a custom time tool.

This project demonstrates how to build a ReAct (Reasoning and Acting) agent using LangChain, LangGraph, and Ollama. The agent can interact with users, answer general queries, and is equipped with a custom tool to fetch and provide the current UTC time when explicitly requested by the user. It is designed to run locally using Ollama for the LLM and can be accessed via a web UI provided by `langgraph dev`.


## Technologies

| Name      | Badge                                                                                                                                                   | Description                                                                                                        |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Python    | [![Python](https://img.shields.io/badge/Python%2DPython?style=flat&logo=python&color=%231f4361)](https://www.python.org/)                               | The core programming language used for the project.                                                                |
| LangChain | [![LangChain](https://img.shields.io/badge/LangChain%2DLangChain?style=flat&logo=langchain&color=%231c3c3c)](https://python.langchain.com/)             | Framework for building LLM applications. Used here for `ChatOllama` and agent creation utilities.                  |
| LangGraph | [![LangGraph](https://img.shields.io/badge/LangGraph%2DLangGraph?style=flat&logo=langchain&color=%23053d5b)](https://langchain-ai.github.io/langgraph/) | Library for building stateful, multi-actor LLM applications. Used for `create_react_agent` to construct the agent. |
| Ollama    | [![Ollama](https://img.shields.io/badge/Ollama%2DOllama?style=flat&logo=ollama&color=%23dc6416)](https://ollama.com/)                                   | Platform for running LLMs locally. Used to serve the `llama3.1` model (or other specified model) for the agent.    |


## Key Features

*   **Local LLM Execution:** Integrates with Ollama to run large language models (e.g., `llama3.1`) locally.
*   **ReAct Agent:** Implements a ReAct agent using LangChain and LangGraph, enabling the LLM to reason and use tools.
*   **Custom Time Tool:** Features a `get_current_time` tool that allows the agent to fetch the current UTC time.
*   **Contextual Tool Usage:** The agent is specifically prompted to:
    *   Use the time tool *only* when the user explicitly asks for the current time.
    *   Avoid using the time tool or mentioning the time for general queries.
*   **Multi-lingual Response:** The agent is instructed to respond in the language used by the user.
*   **Web UI Interaction:** Designed to be run and interacted with via the `langgraph dev` web interface.
*   **Automatic Model Download:** The script attempts to download the specified Ollama model if it's not already available locally.


## Installation

1.  **Prerequisites:**
    *   Ensure you have Python 3.8+ installed.
    *   Install Ollama by following the instructions at [https://ollama.com/](https://ollama.com/). Ensure Ollama is running.

2.  **Clone the repository:**

    ```bash
    git clone https://github.com/oddshellnick/ai_with_get_time_tool
    ```

3.  **Install the required Python packages using pip:**

    ```bash
    pip install -r requirements.txt
    ```


## Usage

The agent is designed to be run using the LangGraph development server, which provides a web interface for interaction.

### Running the Agent

1.  **Ensure Ollama is running:**
    Start your Ollama application. The script will attempt to pull the `llama3.1` model if it's not present.

2.  **Run the agent using LangGraph CLI:**

    ```bash
    langgraph dev
    ```


### Example Interactions (via Web UI)

Once the LangGraph dev server is running and you have accessed the web UI:

*   **User asks for the time:**
    *   **User Input:** `What time is it?`
    *   **Agent Response (example):** `The current time is 2024-07-28T10:30:00Z.`

*   **User asks a general question:**
    *   **User Input:** `Tell me a joke.`
    *   **Agent Response (example):** `Why don't scientists trust atoms? Because they make up everything!`

*   **User asks for the time in another language:**
    *   **User Input (Spanish):** `¿Qué hora es?`
    *   **Agent Response (Spanish, example):** `La hora actual es 2024-07-28T10:32:00Z.`


## Classes and Functions

### `main` module (`main.py`)

This module contains all the logic for setting up the Ollama connection, defining tools, and building the LangGraph agent.

*   **Functions:**
    *   `get_current_time()`:
        *   Retrieves the current Coordinated Universal Time (UTC).
        *   Returns a dictionary with the current time in ISO-8601 format, e.g., `{"utc": "2025-05-21T06:42:00Z"}`.
    *   `setup_ollama(...)`:
        *   Initializes and configures the Ollama LLM.
        *   Checks if the `ollama` command-line tool is installed and accessible. Exits if not.
        *   Attempts to pull the specified `model_name` (e.g., `llama3.1`) using `ollama pull`. Exits on failure.
        *   Returns a `ChatOllama` instance configured with the specified model.
    *   `build_ollama_graph(...)`:
        *   Constructs the LangGraph ReAct agent.
        *   Sets up the Ollama model using `setup_ollama(model_name)`.
        *   Creates a ReAct agent using `langgraph.prebuilt.create_react_agent`.
        *   Integrates the `get_current_time` function as a tool available to the agent.
        *   Includes a system prompt that guides the agent's behavior regarding:
            *   Using the `get_current_time` tool only when explicitly asked for the time.
            *   Responding to the user in the language they used.
*   **Global Variables:**
    *   `graph`: An instance of the compiled LangGraph agent, created by calling `build_ollama_graph(model_name="llama3.1")`. This is the object that `langgraph dev` serves.


## Note

Please be aware that the `test_conditions` folder contains files related to the test assignment. You are welcome to attempt to solve it independently, if you wish.