# Write a python program to find sequences of one uppercase letter followed by lowercase letter.

import re

def find_sequences(text):
    # Pattern to match one uppercase letter followed by one lowercase letter
    pattern = r"[A-Z][a-z]"
    sequences = re.findall(pattern, text)
    return sequences

def main():
    text = input("Enter a text: ")
    sequences = find_sequences(text)

    if sequences:
        print("Sequences of one uppercase letter followed by a lowercase letter:")
        print(sequences)
    else:
        print("No sequences found matching the pattern.")

if __name__ == "__main__":
    main()