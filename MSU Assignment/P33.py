'''Write a program to read two double values from command line, perform division among them and display answer. Handle all possible
errors using Exception Handling mechanism and display appropriate message.(Use one try and multiple catches).'''

import sys

try:
    # Read two double values from the command line
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    result = num1 / num2
    print("Division result:", result)
except IndexError:
    print("Please provide two double values as command line arguments.")
except ValueError:
    print("Please provide valid double values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("An error occurred:", e)