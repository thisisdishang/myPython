# Write a python program to read two files and concate it output and write it in third file.

try:
    file1 = input("Enter the name of the first input file: ")
    file2 = input("Enter the name of the second input file: ")
    path = 'MSU Assignment\\'
    with open(path+file1) as f1:
        content1 = f1.read()
    with open(path+file2) as f2:
        content2 = f2.read()
    concatenated_content = content1 + "\n" + content2
    output_file = input("Enter the name of the output file: ")
    with open(path+output_file, 'w') as f_out:
        f_out.write(concatenated_content)
        print("Concatenated content has been written to", output_file)
except FileNotFoundError:
    print("Error: One of the input files does not exist.")
except Exception as e:
    print("An unexpected error occurred:", e)
