from menu_system import main_menu
from schedule_manager import ScheduleManager
from task_tracker import TaskTracker
from notes_manager import NotesManager

def main():
    schedules = ScheduleManager()
    tasks = TaskTracker()
    notes = NotesManager()
    
    print("=== STUDENT ORGANIZER ===")
    
    while True:
        main_menu()
        choice = input("Choose option (1-4): ")
        
        if choice == "1":
            schedules.manage_schedules()
        elif choice == "2":
            tasks.manage_tasks()
        elif choice == "3":
            notes.manage_notes()
        elif choice == "4":
            print("Goodbye! Stay organized!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()