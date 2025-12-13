from datetime import datetime, time, timedelta
import time


def display_current_datetime ():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_date_time = now.strftime("%I:%M:%S")
    print(f"Current date and time: {current_date} {current_date_time}")

    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = now + timedelta(days=days_to_add)
    print(future_date.strftime("%Y-%m-%d"))


display_current_datetime()
