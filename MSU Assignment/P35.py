# Write a python program to read file contain and if file is not available then handle it using appropriate exception handling

try:
    file_name = input("Enter the file name: ")
    path='MSU Assignment\\'
    with open(path+file_name, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: The file '{}' is not available.".format(file_name))
except Exception as e:
    print("An error occurred:", e)