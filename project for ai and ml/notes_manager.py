from menu_system import notes_menu

class NotesManager:
    def __init__(self):
        self.notes = []
    
    def add_note(self):
        note = input("Enter your note: ")
        self.notes.append(note)
        print("Note added!")
    
    def view_notes(self):
        if not self.notes:
            print("No notes yet!")
            return
        
        print("\n--- YOUR NOTES ---")
        for i, note in enumerate(self.notes):
            print(f"{i+1}. {note}")
    
    def manage_notes(self):
        while True:
            notes_menu()
            choice = input("Choose option: ")
            
            if choice == "1":
                self.add_note()
            elif choice == "2":
                self.view_notes()
            elif choice == "3":
                break
            else:
                print("Invalid choice!")