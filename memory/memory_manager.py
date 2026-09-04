import json
import os

# =========================
# FILE PATH
# =========================

MEMORY_FILE = "active_data.json"

# =========================
# LOAD MEMORY
# =========================

def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return {
            "tosses": [],
            "matches": [],
            "sessions": [],
            "sballs": [],
            "inning_breaks": [],
            "entries": []
        }

    with open(MEMORY_FILE, "r") as file:

        data = json.load(file)

    return data

# =========================
# SAVE MEMORY
# =========================

def save_memory(data):

    # Only reset a memory section when it crosses 100 saved records.
    # Everything else in the bot continues to work exactly as before.
    sections = ("tosses", "matches", "sessions", "sballs", "inning_breaks", "entries")
    for section in sections:
        items = data.get(section)
        if isinstance(items, list) and len(items) > 100:
            newest = items[-1]
            if isinstance(newest, dict):
                newest = newest.copy()
                newest["id"] = 1
            data[section] = [newest]

    with open(MEMORY_FILE, "w") as file:

        json.dump(data, file, indent=4)

# =========================
# RESET MEMORY
# =========================

def reset_memory():

    data = {
        "tosses": [],
        "matches": [],
        "sessions": [],
        "sballs": [],
        "inning_breaks": [],
        "entries": []
    }

    save_memory(data)

# =========================
# GET NEXT ID
# =========================

def get_next_id(section):

    data = load_memory()

    items = data.get(section, [])

    if not items:
        return 1

    return items[-1]["id"] + 1