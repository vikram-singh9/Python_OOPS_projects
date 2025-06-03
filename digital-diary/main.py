import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.date = datetime.datetime.now()

    def display(self):
        print(f"\nTitle: {self.title}")
        print(f"Time: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Content:\n{self.content}")


class Diary:
    def __init__(self):
        self.notes  = []

    def add_note(self, note):
        self.notes.append(note)
        print(f"\nNote: {note.title} added successfully!")

    def display_notes(self):
        if not self.notes:
            print("\nNo notes available.")
        for note in self.notes:
            note.display()

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print(f"\nNote: {title} deleted successfully!")
                return
        print(f"\nNote: {title} not found.")


note1 = Note("Morning Thoughts", "Today I woke up early and felt fresh.")
note2 = Note("Evening Reflection", "It was a productive day.")
note3 = Note("Daily Summary", "I completed all my tasks and learned something new.")
note4 = Note("Weekend Plans", "Planning to go hiking this weekend.")

dairy = Diary()
dairy.add_note(note1)
dairy.add_note(note2)
dairy.add_note(note3)
dairy.add_note(note4)

dairy.display_notes()  # Display all notes

dairy.delete_note("Morning Thoughts")  # Delete a note by title

dairy.display_notes()  # Display notes after deletion



