# Write a python program to convert date of yyyy-mm-dd to dd-mm-yyyy

from datetime import datetime


def convert_date(date_str):
    try:
        # Parse the input date string to a datetime object
        date_object = datetime.strptime(date_str, '%Y-%m-%d')

        # Convert the datetime object to the desired format
        converted_date = date_object.strftime('%d-%m-%Y')
        return converted_date
    except ValueError:
        return "Invalid date format. Please provide the date in yyyy-mm-dd format."

# Example usage
input_date = input("Enter the date in yyyy-mm-dd format: ")
converted_date = convert_date(input_date)
print("Converted date:", converted_date)