from memory.memory_manager import *

# =========================
# LOAD MEMORY
# =========================

data = load_memory()

# =========================
# CREATE MULTIPLE TOSSES
# =========================

toss1 = {
    "id": get_next_id("tosses"),
    "match": "IND vs AUS",
    "winner": "IND",
    "status": "pending"
}

data["tosses"].append(toss1)

# -------------------------

toss2 = {
    "id": get_next_id("tosses"),
    "match": "PAK vs ENG",
    "winner": "PAK",
    "status": "pending"
}

data["tosses"].append(toss2)

# -------------------------

toss3 = {
    "id": get_next_id("tosses"),
    "match": "CSK vs MI",
    "winner": "CSK",
    "status": "pending"
}

data["tosses"].append(toss3)

# =========================
# SAVE MEMORY
# =========================

save_memory(data)

print("\n✅ 3 TEST TOSSES SAVED\n")