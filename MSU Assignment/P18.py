# Python code to sort a sequence of names according to their alphabetical order without using sort() function

namelist=['Bryer','Ellie','Aeris','Piren','Ehan'] 
print("Original List:", namelist)
 
# sorting list using nested loops
for i in range(0, len(namelist)):
    for j in range(i+1, len(namelist)):
        if namelist[i] >= namelist[j]:
            namelist[i], namelist[j] = namelist[j],namelist[i]

print("Sorted List", namelist)