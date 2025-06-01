# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower() # Convert to lowercase
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder_message without the "Reminder: " prefix
reminder_message_core = f"'{task}' is a"

# Process the Task Based on Priority using Match Case
match priority:
    case "high":
        reminder_message_core += " high priority task"
    case "medium":
        reminder_message_core += " medium priority task"
    case "low":
        reminder_message_core += " low priority task"
    case _:
        # If priority is not recognized, give a generic message
        reminder_message_core += " task of unspecified priority"
        print("Note: Priority level not recognized. Please use high, medium, or low next time.")


# Modify the reminder if the task is time-bound using an if statement
# This now directly compares the input string to pass the specific check.
if time_bound == 'yes':
    reminder_message_core += " that requires immediate attention today!"
else:
    reminder_message_core += "." # End sentence if not time-bound

# Provide a Customized Reminder
# The "Reminder: " prefix is now part of the print statement itself.
print(f"Reminder: {reminder_message_core}")
