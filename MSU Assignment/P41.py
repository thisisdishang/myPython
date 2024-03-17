# Write a python program to find occurrence and position of substrings within a string

def find_occurrences_positions(string, substring):
    occurrences = []
    position = string.find(substring)
    while position != -1:
        occurrences.append(position)
        position = string.find(substring, position + 1)
    return occurrences

def main():
    string = input("Enter a string: ")
    substring = input("Enter a substring to search: ")
    occurrences_positions = find_occurrences_positions(string, substring)

    if len(occurrences_positions) == 0:
        print("Substring not found in the string.")
    else:
        print("Occurrences of substring '{}' in the string:".format(substring))
        for i, pos in enumerate(occurrences_positions, start=1):
            print("Occurrence {}: Position {}".format(i, pos))


if __name__ == "__main__":
    main()