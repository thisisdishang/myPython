# Python program to count no of vowels using set in a given string

count = 0
mystr = input("Enter the string:")
vowel = set('aeiouAEIOU')
for i in mystr:
    if i in vowel:
        count += 1

print(count)