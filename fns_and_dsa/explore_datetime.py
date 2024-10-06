import datetime
def display_current_datetime() :
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")
display_current_datetime()

from datetime import timedelta
def calculate_future_date() :
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.datetime.now()
    future_date = current_date + timedelta(days = number_of_days )
    formated_future_date = future_date.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Future date: {formated_future_date}")
calculate_future_date()