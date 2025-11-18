task = input('Enter task description: ')
priority = input('Is the task high/medium/low? ') 
time_bound = input('Is the task time-bound(yes/no)? ')

match priority:
    case 'high':
        if priority == 'high' and time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif priority == 'high' and time_bound != 'yes':
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print('Incorrect details')
    case 'medium':
        if priority == 'medium' and time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif priority == 'medium' and time_bound != 'yes':
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print('Incorrect details')
    case 'low':
        if priority == 'low' and time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif priority == 'low' and time_bound != 'yes':
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print('Incorrect details')