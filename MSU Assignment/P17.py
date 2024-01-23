# Python program that accepts a sentence and calculate the number of digits, uppercase and lowercase letters

s=input("Enter the sentence:")
d=u=l=0
for i in s:
    if i.isdigit():
        d+=1
    elif i.isupper():
        u+=1
    elif i.islower():
        l+=1

print(f"Total number of digit is {d}")
print(f"Total number of uppercase letter is {u}")
print(f"Total number of lowercase letter is {l}")