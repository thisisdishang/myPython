# Python program to count the total number of vowels, consonants and blanks in a String

s=input("Enter the string: ")
conso=vow=blank=0

for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U':
        vow+=1
    elif i==" ":
        blank+=1
    else:
        conso+=1

print("Total Number of Vowels is:",vow)
print("Total Number of Consonants is:",conso)
print("Total Number of Blanks is:",blank)