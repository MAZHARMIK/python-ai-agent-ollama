<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6366f1,100:ec4899&height=220&section=header&text=Local%20AI%20Agent&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Python%20%C2%B7%20Ollama%20%C2%B7%20Tool%20Calling%20%E2%80%94%20built%20from%20scratch&descAlignY=55&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=800&color=A78BFA&center=true&vCenter=true&width=750&lines=An+AI+agent+that+runs+100%25+on+your+laptop+%F0%9F%92%BB;No+paid+API+key.+No+agent+framework.;It+remembers%2C+uses+tools+and+chains+them+%F0%9F%94%A7;Built+from+scratch+with+python-ai-agent-ollama" alt="Typing SVG"/>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)
![OpenAI API](https://img.shields.io/badge/OpenAI--compatible-API-412991?style=for-the-badge&logo=openai&logoColor=white)
![Qwen3](https://img.shields.io/badge/Model-qwen3:4b-6366f1?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)

<a href="https://www.youtube.com/watch?v=fMHGSx8B9gs&list=PLUqOqHuQynYk">
  <img src="https://img.shields.io/badge/Playlist-AI_Fundamentals-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="AI Fundamentals playlist"/>
</a>
<a href="https://www.youtube.com/watch?v=f0HBW-47wwU&list=PLGSKQmIKK2zQ">
  <img src="https://img.shields.io/badge/Playlist-Advanced_AI-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Advanced AI playlist"/>
</a>

</div>

<br/>

## 🚀 What is this?

<img src="https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/codestorywithmik.png?raw=true" align="right" width="320"/>

A **local AI agent built from scratch in Python**. It talks to a model running on [Ollama](https://ollama.com) through the OpenAI-compatible API, so there is **no paid key and no framework** hiding the logic.

It remembers the conversation, follows a system prompt, and can use tools **in several steps**. For example, it first finds your city, then fetches the weather for that city.

> 🎬 Built as part of the **Advanced AI** series on [codestorywithMIK](https://www.youtube.com/@codestorywithMIK).

> 📚 **New to AI?** Start with the [AI Fundamentals playlist](https://www.youtube.com/watch?v=fMHGSx8B9gs&list=PLUqOqHuQynYk) (tokens, embeddings, vector databases, RAG), then follow the [Advanced AI playlist](https://www.youtube.com/watch?v=f0HBW-47wwU&list=PLGSKQmIKK2zQ) where this project is built step by step.

> [!NOTE]
> 🌱 **Work in progress:** This project is in its early phase. As the Advanced AI playlist moves ahead, it will keep evolving, and we will add things like **RAG**, persistent memory and more tools.

<br clear="right"/>

<br/>

## 🎥 See it in action

<img width="757" height="317" alt="Screenshot 2026-10-20 at 1 54 28 AM" src="https://github.com/user-attachments/assets/f314ca05-5399-4e96-9ae8-32515d55a235" />


<div align="center"><sub>The grey lines are the debug trace: you can watch the agent think.</sub></div>

<br/>

## ✨ Features

| | Feature | Details |
|---|---|---|
| 🧠 | **Conversation memory** | The full history is sent on every call, because the model itself has no memory |
| 🎭 | **System prompt** | Sets the agent's behavior and style |
| 🔧 | **Tool calling** | Tools are described with JSON schema and run by our own code |
| 🔗 | **Chained tool calls** | A loop with a step limit (`MAX_STEPS = 5`) so it can never run forever |
| 📝 | **Required parameters** | `get_city_weather` needs a `city`, declared in the schema |
| 🛡️ | **Safe errors** | Tool failures go back to the model as text, so the program does not crash |
| 🪲 | **Debug trace** | Grey step-by-step logs, switched on with `DEBUG=True` |

<br/>

## 🧩 How it works

The model **never runs code**. It only asks for a tool. Our Python code runs it, sends the result back, and the loop repeats until the model answers in plain text.

```mermaid
flowchart LR
    U([You]) --> M[simple_ai_assistant.py]
    M -->|history and tool list| L{{LLM on Ollama}}
    L -->|tool request| R[tools.run_tool]
    R --> T1[get_current_time]
    R --> T2[get_city_weather]
    R --> T3[get_user_city]
    T1 -->|result as text| M
    T2 -->|result as text| M
    T3 -->|result as text| M
    L -->|final answer| A([Assistant])
```

<details>
<summary><b>📖 The 4-step loop in words (click to expand)</b></summary>

1. We send the conversation plus the list of tools to the model.
2. The model replies with a **request** such as `get_city_weather(city="Bangalore")`, not an answer.
3. Our code runs the real function and sends the result back with the `tool` role.
4. The model reads the result and either asks for another tool or writes the final answer.

This repeats up to `MAX_STEPS` times per question.

</details>

<br/>

## 🛠️ Available tools

| Tool | What it does |
|---|---|
| `get_current_time` | Returns the current local date and time |
| `get_city_weather(city)` | One-line weather from the free `wttr.in` service |
| `get_user_city` | Returns the user's city (hard-coded to `Bangalore` as a demo value) |

<br/>

## ⚡ Quick start

**Prerequisites:** Python 3.10+ and [Ollama](https://ollama.com/download) installed and running.

```bash
# 1. Download the model
ollama pull qwen3:4b

# 2. Get the code
git clone https://github.com/MAZHARMIK/python-ai-agent-ollama.git
cd python-ai-agent-ollama

# 3. Create and activate a virtual environment
python -m venv .venv
# Windows:    .venv\Scripts\activate
# Mac/Linux:  source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create your settings file
cp .env.example .env        # Windows: copy .env.example .env

# 6. Run
python simple_ai_assistant.py
```

Type `exit`, `quit`, `bye` or `goodbye` to stop.

<!-- SCREENSHOT 2: the terminal after step 6, showing the first prompt. -->
<img width="490" height="165" alt="Screenshot 2026-10-20 at 1 57 07 AM" src="https://github.com/user-attachments/assets/3a0a7993-d71a-4caa-a470-49fcdd02861a" />


<br/>

## ⚙️ Configuration

Settings live in `.env` (see `.env.example`):

| Name | Meaning |
|---|---|
| `BASE_URL` | OpenAI-compatible endpoint. For Ollama: `http://127.0.0.1:11434/v1` |
| `API_KEY` | Required by the client, ignored by Ollama. Any dummy value works |
| `MODEL` | Exact model name from `ollama list`. It must support tool calling |
| `DEBUG` | Set to `True` (capital T) to show the grey debug trace |

> 💡 Rules for `.env`: `NAME=value`, no spaces around `=`, no quotes. Restart the program after editing it.

<br/>

## 📸 More screenshots

<img width="490" height="165" alt="Screenshot 2026-10-20 at 1 58 20 AM" src="https://github.com/user-attachments/assets/b56a8a7f-b1c6-46ff-bc02-13b0c1901d5c" />
<br/>

<img width="490" height="165" alt="Screenshot 2026-10-20 at 2 02 02 AM" src="https://github.com/user-attachments/assets/c1719353-4edb-4c08-9f8e-78260dda1de9" />

<br/>

## ➕ Add your own tool

Three changes in `tools.py`, and the chat loop stays untouched:

1. ✍️ Write the Python function.
2. 📋 Add its description to the `TOOLS` list (name, description, parameters, `required`).
3. 🗺️ Register it in `FUNCTION_NAME_TO_FUNCTION_MAP`.

> The `description` matters: the model reads it to decide when to use the tool.

<br/>

## 📁 Project structure

```text
python-ai-agent-ollama/
├── simple_ai_assistant.py    chat loop, memory and the agent loop
├── tools.py                  tool functions, TOOLS schema, run_tool()
├── Utilities/
│   └── utilities.py          grey debug log() helper
├── .env.example              settings template
├── requirements.txt          dependencies
└── LICENSE                   MIT
```

<br/>

## ⚠️ Honest limitations

- Memory is kept in RAM and is lost when the program exits.
- The history is not trimmed, so very long chats can exceed the model's context window.
- Small local models can pick the wrong tool or skip arguments. A larger model is more reliable.
- `get_user_city` is a hard-coded demo value. In a real app it would come from a profile or database.
- The weather tool needs internet, and `wttr.in` is a free service that can be slow or down.
- Tool output is not treated as untrusted, which is why the tools are read-only.

<br/>

## 🎬 Video series

| # | Topic |
|---|---|
| 1 | Roadmap to master Advanced AI |
| 2 | Setup: VS Code, Python, Ollama |
| 3 | First AI call, OpenAI-style API |
| 4 | `.env`, chat loop, roles |
| 5 | Memory and context window |
| 6 | System prompt and prompt engineering basics |
| 7 | Tool calling |
| 8 | Tool with parameters (weather) |
| 9 | Chained tool calls |
| 10 | Refactoring, debug logging, bug fixes |

| Playlist | What it covers |
|---|---|
| ▶️ [**AI Fundamentals**](https://www.youtube.com/watch?v=fMHGSx8B9gs&list=PLUqOqHuQynYk) | Tokens, embeddings, vector databases and RAG. Watch this first if the basics are new to you |
| ▶️ [**Advanced AI**](https://www.youtube.com/watch?v=f0HBW-47wwU&list=PLGSKQmIKK2zQ) | This project, built step by step (videos 1 to 10 in the table above) |

<br/>

<div align="center">

### 🙌 If this helped you, a ⭐ goes a long way. Thank you!

[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@codestorywithMIK)
[![WhatsApp](https://img.shields.io/badge/WhatsApp_Channel-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029Va6kVSjICVfiVdsHgi1A)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/codestorywithmik/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mazhar-imam-khan-95a34ab3/)

<sub>Licensed under <a href="LICENSE">MIT</a></sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ec4899,100:6366f1&height=120&section=footer" width="100%"/>

</div>
