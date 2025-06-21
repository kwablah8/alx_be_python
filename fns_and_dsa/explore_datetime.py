import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.date.today()
    return(datetime.datetime.now())

current_date_and_time = display_current_datetime()
print("Current date and time:", current_date_and_time)

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = current_date_and_time + timedelta(days=number_of_days)
    return(future_date)

future_date = calculate_future_date()
print("Future date:", future_date)