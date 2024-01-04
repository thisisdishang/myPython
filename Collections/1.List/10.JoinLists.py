# There are several ways to join, or concatenate, two or more lists in Python
# One of the easiest ways are by using the + operator
alpha=["A","B","C"]
num=[1,2,3]
opr=["+","-","/"]
join=alpha+num+opr
print(join)

# Another way to join two lists is by appending all the items from list2 into list1, one by one
alpha=["A","B","C"]
num=[1,2,3]

for i in alpha:
    num.append(i)  # type: ignore

print(num)

# You can use the extend() method, where the purpose is to add elements from one list to another list
alpha=["A","B","C"]
num=[1,2,3]
alpha.extend(num) # type: ignore
print(alpha)