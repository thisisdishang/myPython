# Write a function to calculate the power of number raised to other

def calculate_power(base, exponent):
    result = pow(base, exponent)
    return result

base = 2
exponent = 3
power = calculate_power(base, exponent)
print(f"{base} raised to the power of {exponent} is {power}")