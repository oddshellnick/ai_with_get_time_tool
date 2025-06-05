import sys
import warnings
import subprocess
from datetime import datetime, timezone
from langchain_ollama import ChatOllama
from langgraph.graph.graph import CompiledGraph
from langgraph.prebuilt import create_react_agent


def get_current_time() -> dict[str, str]:
    """
    Return the current UTC time in ISO‑8601 format.
    Example → {"utc": "2025‑05‑21T06:42:00Z"}
    """

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    return {"utc": now.replace("+00:00", "Z")}


def setup_ollama(model_name: str) -> ChatOllama:
    """
    Sets up the Ollama environment by checking installation and pulling the specified model.

    Args:
        model_name (str): The name of the Ollama model to set up (e.g., "qwen3:8b").

    Returns:
        ChatOllama: An instance of the ChatOllama model ready for use.
    """

    try:
        subprocess.run(["ollama", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        warnings.warn("Error: Ollama is not installed. Please install it from https://ollama.com/ and try again.")
        sys.exit(1)

    try:
        subprocess.run(["ollama", "pull", model_name], check=True)
    except subprocess.CalledProcessError:
        warnings.warn(f"Error pulling model '{model_name}'. Check your internet connection and model name.")
        sys.exit(1)

    return ChatOllama(model=model_name)


def build_ollama_graph(model_name: str) -> CompiledGraph:
    """
    Builds a Langgraph agent using the specified Ollama model and the get_current_time tool.

    Sets up the Ollama model using setup_ollama and then creates a React agent
    configured to use the model and the time tool with a specific prompt.

    Args:
        model_name (str): The name of the Ollama model to use for the agent (e.g., "qwen3:8b").

    Returns:
        CompiledGraph: A compiled Langgraph agent ready to process inputs.
    """

    model = setup_ollama(model_name=model_name)

    return create_react_agent(
        model=model,
        tools=[get_current_time],
        prompt="""
        You are an assistant that provides helpful responses to user queries.
        Always translate answer to user's language.
        
        Use the 'get_current_time' tool only when the user explicitly asks for the current time.
        When the tool is used, include the time in your response without formatting.
        If the user does not ask for the time, do not use the tool or include the time.
        
        For example:
        - If the user asks, 'What time is it?', use the tool and respond with 'The current time is [time without formatting (YYYY‑MM‑DDTHH:MM:SSZ)].'
        - If the user asks, 'Сколько времени?', use the tool and respond with 'Текущее время [time without formatting (YYYY‑MM‑DDTHH:MM:SSZ)].'
        - If the user says, 'Tell me a joke,' respond with a joke without including the time.
        
        Ensure that the time is only included when the user specifically requests it.
        """
    )


graph = build_ollama_graph(model_name="qwen3:8b")
