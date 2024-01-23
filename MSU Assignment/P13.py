# Python code to check if a given year is a leap year or not

year=int(input("Enter the year to check:"))

if year%4==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")