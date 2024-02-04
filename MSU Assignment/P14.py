# Python program to find the GCD of two positive numbers

import math

a,b=input("Enter two numbers: ").split()
print(f"Greatest Common Divisor of {a} & {b} is",math.gcd(int(a),int(b)))