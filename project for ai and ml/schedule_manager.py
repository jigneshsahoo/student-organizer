from menu_system import schedule_menu

class ScheduleManager:
    def __init__(self):
        self.classes = []
    
    def add_class(self):
        course = input("Enter course name: ")
        time = input("Enter class time (e.g., 9:00 AM): ")
        day = input("Enter day (e.g., Monday): ")
        
        new_class = {
            'course': course,
            'time': time,
            'day': day
        }
        self.classes.append(new_class)
        print(f"Added {course} to your schedule!")
    
    def view_schedule(self):
        if not self.classes:
            print("No classes scheduled yet!")
            return
        
        print("\n--- YOUR WEEKLY SCHEDULE ---")
        for i, class_item in enumerate(self.classes):
            print(f"{i+1}. {class_item['course']} - {class_item['day']} at {class_item['time']}")
    
    def manage_schedules(self):
        while True:
            schedule_menu()
            choice = input("Choose option: ")
            
            if choice == "1":
                self.add_class()
            elif choice == "2":
                self.view_schedule()
            elif choice == "3":
                break
            else:
                print("Invalid choice!")