# Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops

# If:
# An "if statement" is written by using the if keyword
a=20
b=10
if a>b:
    print("a is greater than b")

"""Note:Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
Other programming languages often use curly-brackets for this purpose"""

# Else:
# The else keyword catches anything which isn't caught by the preceding conditions
a=15
if a>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

# Elif:
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition"
# You can also have an else without the elif
a=15
b=15
if a>b:
    print("a is greater than b")
elif a==b:
    print("a and b both are equal")
else:
    print("b is greater than a")

# Short Hand If:
# If you have only one statement to execute, you can put it on the same line as the if statement
a=100
b=24
if a>b:print("a is greater than b")

# Short Hand If ... Else:
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
# This technique is known as Ternary Operators, or Conditional Expressions
A=30
B=30
print("A and B are not equal") if A!=B else print("A and B are equal")

# You can also have multiple else statements on the same line
x=20
y=20
print("x is greater than y") if x>y else print("x and y are equal") if x==y else print("y is greater than x")

# 70And:
# The and keyword is a logical operator, and is used to combine conditional statements
a=100
b=20
c=30
if a>b and b<c:
    print("Both Condition is true...")
else:
    print("Both Condition is not true...")

# Or:
# The or keyword is a logical operator, and is used to combine conditional statements
a=450
b=300
c=100
if a<b or b>c:
    print("At least one condition is true...")
else:
    print("Both condition is false...")

# Not:
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement
a=10
b=45
if not a>b:
    print("a is not greater than b")
else:
    print("b is not greater than a")

# Nested If:
# You can have if statements inside if statements, this is called nested if statements
x=25
if x>18:
    print("x is greater than 18,")
    if x>=25:
        print("and also a mature person")
    else:
        print("but not mature person")