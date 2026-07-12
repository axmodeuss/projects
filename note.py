import sqlite3


class DataBase:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT
            )
        """)
        self.conn.commit()

    def add_note(self):
        new_note_title = input("Enter your new note's title: ").strip()
        new_note = input("Enter your new note: ").strip()

        if new_note_title and new_note:
            self.cursor.execute(
                "INSERT INTO notes(title, content) VALUES (?, ?)",
                (new_note_title, new_note)
            )
            self.conn.commit()
            return "Note added successfully."

        return "Invalid input."

    def show_note(self):
        self.cursor.execute("SELECT * FROM notes")
        rows = self.cursor.fetchall()

        if not rows:
            print("No notes found.")
            return

        print("\n------ Notes ------")
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Title: {row[1]}")
            print(f"Content: {row[2]}")
            print("-" * 30)

    def delete_note(self):
        id_delete = input("Enter id of the note you want to delete: ").strip()

        self.cursor.execute(
            "SELECT * FROM notes WHERE id = ?",
            (id_delete,)
        )

        row = self.cursor.fetchone()

        if row:
            self.cursor.execute(
                "DELETE FROM notes WHERE id = ?",
                (id_delete,)
            )
            self.conn.commit()
            return "Note deleted successfully."

        return "Note not found."

    def update_note(self):
        id_update = input("Enter id of the note you want to update: ").strip()

        self.cursor.execute(
            "SELECT * FROM notes WHERE id = ?",
            (id_update,)
        )

        row = self.cursor.fetchone()

        if not row:
            return "Note not found."

        new_title = input("Enter new title: ").strip()
        new_note = input("Enter new note: ").strip()

        if not new_title or not new_note:
            return "Invalid input."

        self.cursor.execute(
            """
            UPDATE notes
            SET title = ?, content = ?
            WHERE id = ?
            """,
            (new_title, new_note, id_update)
        )

        self.conn.commit()
        return "Data updated successfully."

    def close(self):
        self.conn.close()


db = DataBase("notes.db")
db.create_table()

while True:
    print("\n===== Notes App =====")
    print("1. Add Note")
    print("2. Show Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")

    choice = input("Choose: ").strip()

    if choice == "1":
        print(db.add_note())

    elif choice == "2":
        db.show_note()

    elif choice == "3":
        print(db.update_note())

    elif choice == "4":
        print(db.delete_note())

    elif choice == "5":
        db.close()
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")