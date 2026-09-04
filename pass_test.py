from memory.memory_manager import *

# =========================
# LOAD MEMORY
# =========================

data = load_memory()

# =========================
# PASS TOSS ID
# =========================

pass_id = 1

# =========================
# FIND TOSS
# =========================

found = False

for toss in data["tosses"]:

    if toss["id"] == pass_id:

        toss["status"] = "passed"

        found = True

        print(f"\n✅ TOSS ID {pass_id} PASSED\n")

# =========================
# SAVE MEMORY
# =========================

save_memory(data)

# =========================
# NOT FOUND
# =========================

if not found:

    print("\n❌ TOSS NOT FOUND\n")