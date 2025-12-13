from datetime import datetime, time, timedelta
import time


def display_current_datetime ():
    now = datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date_time}")

    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date = now + timedelta(days=number_of_days)
    print(calculate_future_date.strftime("%Y-%m-%d"))


display_current_datetime()
