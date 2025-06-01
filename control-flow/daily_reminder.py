# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower() # Convert to lowercase
time_bound_input = input("Is it time-bound? (yes/no): ").lower()

# Basic check for time_bound input (simpler than full validation)
is_time_bound = False # Assume not time-bound by default
if time_bound_input == 'yes':
    is_time_bound = True

reminder_message = f"Reminder: '{task}' is a"

# Process the Task Based on Priority using Match Case
match priority:
    case "high":
        reminder_message += " high priority task"
    case "medium":
        reminder_message += " medium priority task"
    case "low":
        reminder_message += " low priority task"
    case _:
        # If priority is not recognized, give a generic message
        reminder_message += " task of unspecified priority"
        print("Note: Priority level not recognized. Please use high, medium, or low next time.")


# Modify the reminder if the task is time-bound using an if statement
if is_time_bound:
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += "." # End sentence if not time-bound

# Provide a Customized Reminder
print(reminder_message)