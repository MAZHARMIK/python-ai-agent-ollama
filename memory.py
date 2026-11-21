import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

CHAT_FOLDER = os.getenv("CHAT_FOLDER")


# Save a chat. path=None means a brand new chat, so we create a file name.
# Returns the path of the chat file
def save_chat(path, messages):
    os.makedirs(CHAT_FOLDER, exist_ok=True)

    if path is None:
        fileName = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        path = os.path.join(CHAT_FOLDER, f"{fileName}.json")

    data = {
        "title": messages[0]["content"][:40],
        "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "messages": messages,
    }

    # Write to a temporary file first, then replace the real file in one step
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp_path, path)

    return path


# Load one chat. Returns None if the file is missing, broken or not a chat.
def load_chat(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


# List saved chats, most recently used first.
def list_chats():
    if not os.path.exists(CHAT_FOLDER):
        return []

    chats = []
    for chat_file_name in os.listdir(CHAT_FOLDER):
        if not chat_file_name.endswith(".json"):
            continue

        path = os.path.join(CHAT_FOLDER, chat_file_name)
        data = load_chat(path)
        if data is None:
            print(f"Skipped unreadable chat file: {chat_file_name}")
            continue

        chats.append(
            {
                "path": path,
                "title": data.get("title", "(untitled)"),
                "updated": data.get("updated", ""),
                "count": len(data["messages"]),
            }
        )

    chats.sort(key=lambda c: c["updated"], reverse=True)
    return chats



