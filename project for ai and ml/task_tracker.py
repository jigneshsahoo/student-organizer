from menu_system import task_menu

class TaskTracker:
    def __init__(self):
        self.tasks = []
    
    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append({'task': task, 'completed': False})
        print(f"Added: {task}")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return
        
        print("\n--- YOUR TASKS ---")
        for i, task in enumerate(self.tasks):
            status = "✓" if task['completed'] else "☐"
            print(f"{i+1}. {status} {task['task']}")
    
    def mark_complete(self):
        self.view_tasks()
        if self.tasks:
            try:
                task_num = int(input("Enter task number to mark complete: ")) - 1
                if 0 <= task_num < len(self.tasks):
                    self.tasks[task_num]['completed'] = True
                    print("Task marked complete! ✓")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")
    
    def manage_tasks(self):
        while True:
            task_menu()
            choice = input("Choose option: ")
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_complete()
            elif choice == "4":
                break
            else:
                print("Invalid choice!")