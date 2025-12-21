# daily_reminder.py

# 1. Prompt for Task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# 2. Process based on Priority (Match Case)
match priority:
    case "high":
        # 3. Check Time Sensitivity (If statement)
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task, but not urgent.")
            
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a medium priority task.")

    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")

    case _:
        print("Error: Unknown priority level. Please enter high, medium, or low.")