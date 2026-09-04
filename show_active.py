from memory.memory_manager import *

# =========================
# LOAD MEMORY
# =========================

data = load_memory()

# =========================
# SHOW ACTIVE TOSSES
# =========================

print("\n🔥 ACTIVE TOSSES 🔥\n")

tosses = data["tosses"]

if not tosses:

    print("❌ NO ACTIVE TOSSES")

else:

    for toss in tosses:

        print(
            f'ID : {toss["id"]} | '
            f'{toss["match"]} | '
            f'WINNER : {toss["winner"]} | '
            f'STATUS : {toss["status"]}'
        )