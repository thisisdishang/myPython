'''Write a password generator function in python which should generate random passwords every time the user ask for a new password.
Strong password should be a mix of lower case, uppercase, number and symbol'''

import random
import string

def generate_password(length=12):
    # Define the character sets for each type of character
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + symbols
    
    # Generate a password with a mix of lowercase, uppercase, digits, and symbols
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

new_password = generate_password()
print("Generated Password:", new_password)