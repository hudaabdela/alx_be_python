task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")
match priority :
    case "high" :
        if time == "yes" :
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "low" :
        if time == "no" :
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
                    