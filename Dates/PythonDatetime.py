# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects
import datetime

d=datetime.datetime.now()
print(d)

# Date Output
# The date contains year, month, day, hour, minute, second, and microsecond
# The datetime module has many methods to return information about the date object
print(d.year)
print(d.strftime("%A"))

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module
# The datetime() class requires three parameters to create a date: year, month, day
'''The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
but they are optional, and has a default value of 0, (None for timezone)'''
d=datetime.datetime(2020,2,5)
print(d)

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string
x = datetime.datetime(2020, 2, 5)
print(x.strftime("%B"))