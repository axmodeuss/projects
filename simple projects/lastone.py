import json
import os

if os.path.exists("notes.json"):
    with open("notes.json", "r") as file:
        notes = json.load(file)
    print("📂 Previous notes loaded successfully!")
else:
    notes = []
    print("✨ No previous notes found. Started a new list.")

if notes:
    print("\n--- Your Current Notes ---")
    for index, note in enumerate(notes, 1):
        print(f"📄 {index}. {note}")

print("\n--- Add New Notes ---")
for note in range(3):
    new_note = input(f"Enter note {note + 1}: ")
    notes.append(new_note)

with open("notes.json", "w") as file:
    json.dump(notes, file, indent=4)

print("\n💾 All notes saved successfully!")