# You can convert from one type to another with the int(), float(), and complex() methods

x = 5    # int
y = 8.8  # float
z = 91j   # complex
w = "5" # String

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)
e = int(w)

#convert from int to complex:
c = complex(x)
d = complex(y)

print(a)
print(b)
print(c)
print(d)
print(e)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# You cannot convert complex numbers into another number type