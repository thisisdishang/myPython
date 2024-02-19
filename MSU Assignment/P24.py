# Given a list of tuples containing both int and string remove all the string from list of tuples

def check(x):
    return not isinstance(x, str)


list1 = [('Rana', 1), ('Corporation', 2), ('Foundation', 3)]

output = ([tuple(filter(check, x)) for x in list1])
print(output)