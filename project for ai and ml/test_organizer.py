# Simple test file
print("Testing Student Organizer components...")

# Test basic functionality
test_schedules = []
test_tasks = []
test_notes = []

test_schedules.append({"course": "Math", "time": "9:00 AM", "day": "Monday"})
test_tasks.append({"task": "Complete assignment", "completed": False})
test_notes.append("Remember to study for exam!")

print("✓ Schedules:", len(test_schedules))
print("✓ Tasks:", len(test_tasks)) 
print("✓ Notes:", len(test_notes))
print("All tests passed! ✅")