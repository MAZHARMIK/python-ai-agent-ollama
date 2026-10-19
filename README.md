# python-ai-agent-ollama

A local AI agent built from scratch in Python. It runs on [Ollama](https://ollama.com) through the OpenAI-compatible API, so it needs no paid API key and no agent framework.

It remembers the conversation, follows a system prompt, and can call tools in several steps. For example, it can first look up the user's city and then fetch the weather for that city.

Built as part of the **Advanced AI** series on [codestorywithMIK](https://www.youtube.com/@codestorywithMIK).

## Features

- Chat loop with conversation memory (the full history is sent on every call)
- System prompt that sets the agent's behavior
- Tool calling (function calling) with JSON-schema tool descriptions
- Chained tool calls in a loop with a step limit (`MAX_STEPS = 5`)
- A tool with a required parameter (`get_city_weather`)
- Tool errors are returned to the model as text, so the program does not crash
- Optional grey debug trace of tool calls, controlled by `DEBUG` in `.env`

## Demo

Example session with `DEBUG=True` (output varies by model):

```text
👦🏻 MIK: What is the weather in the city where I live?
  Step 1: model requested 1 tool calls
  🔧 get_user_city({})
     ↳ Bangalore
  Step 2: model requested 1 tool calls
  🔧 get_city_weather({'city': 'Bangalore'})
     ↳ Bangalore: ☀️ +26°C
🤖 Assistant: Sunny and 26 degrees in Bangalore.
```

The grey lines are the debug trace. With debug off, only the final answer is shown.

## How it works

The model never runs code. It only asks for a tool. Our Python code runs the tool, sends the result back, and repeats until the model answers in plain text or the step limit is reached.

```text
user question -> model (with tool list)
   -> tool requested? yes -> run tool -> send result back -> model again
                      no  -> final answer
```

## Quick start

Prerequisites: Python 3.10+ and [Ollama](https://ollama.com/download) installed and running.

```bash
ollama pull qwen3:4b

git clone https://github.com/MAZHARMIK/python-ai-agent-ollama.git
cd python-ai-agent-ollama

python -m venv .venv
# Windows:    .venv\Scripts\activate
# Mac/Linux:  source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env        # Windows: copy .env.example .env

python simple_ai_assistant.py
```

Type `exit`, `quit`, `bye` or `goodbye` to stop.

## Configuration

Settings live in `.env` (see `.env.example`):

| Name | Meaning |
|---|---|
| `BASE_URL` | OpenAI-compatible endpoint. For Ollama: `http://127.0.0.1:11434/v1` |
| `API_KEY` | Required by the client, ignored by Ollama. Use any dummy value |
| `MODEL` | Exact model name from `ollama list`. The model must support tool calling |
| `DEBUG` | Set to `True` (exactly, with a capital T) to show the grey debug trace |

Rules for `.env`: `NAME=value`, no spaces around `=`, no quotes. Restart the program after editing it.

## Available tools

| Tool | What it does |
|---|---|
| `get_current_time` | Returns the current local date and time |
| `get_city_weather(city)` | Returns a one-line weather summary from the free `wttr.in` service |
| `get_user_city` | Returns the user's city (hard-coded to `Bangalore` as a demo value) |

## Add your own tool

Three changes in `tools.py`, and the chat loop stays untouched:

1. Write the Python function.
2. Add its description to the `TOOLS` list (name, description, parameters, `required`).
3. Register it in `FUNCTION_NAME_TO_FUNCTION_MAP`.

The `description` matters: the model reads it to decide when to use the tool.

## Project structure

```text
simple_ai_assistant.py    chat loop, memory, and the agent loop
tools.py                  tool functions, TOOLS schema, run_tool()
Utilities/utilities.py    grey debug log() helper
.env.example              settings template
requirements.txt          Python dependencies
```

## Limitations

- Memory is kept in RAM and is lost when the program exits.
- The history is not trimmed, so very long chats can exceed the model's context window.
- Small local models can pick the wrong tool or skip arguments. A larger model is more reliable.
- `get_user_city` is a hard-coded demo value. In a real app it would come from a profile or database.
- The weather tool needs internet, and `wttr.in` is a free service that can be slow or down.
- Tool output is not treated as untrusted, so the tools are read-only on purpose.

## Video series

| Topic | Video |
|---|---|
| Roadmap | 1 |
| Setup: VS Code, Python, Ollama | 2 |
| First AI call, OpenAI-style API | 3 |
| `.env`, chat loop, roles | 4 |
| Memory and context window | 5 |
| System prompt | 6 |
| Tool calling | 7 |
| Tool with parameters | 8 |
| Chained tool calls | 9 |
| Refactoring and debug logging | 10 |

Playlist: [codestorywithMIK on YouTube](https://www.youtube.com/@codestorywithMIK)

## License

[MIT](LICENSE)
