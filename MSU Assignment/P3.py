# Python program to generate two random number and perform left and right shift of generated number
import random
a=random.randint(1,11)
b=random.randint(1,11)
print("Random Number 1 is ",a)
print("Random Number 2 is ",b)
print("Number 1 Left shift is ",a<<1," Right shift is ",a>>1)
print("Number 2 Left shift is ",b<<1," Right shift is ",b>>1)