'''Write a method to compute addition of two matrices to get a resultant matrix. Call this method in main to have
A= B+C+D(where A,B,C,D are matrices).'''
# a) Use command line arguments
# b) Raise and handle define exception if size of matrix is improper for doing matrix addition

class MatrixSizeError(Exception):
    pass

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise MatrixSizeError("Matrix sizes are not compatible for addition")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def main():
    try:
        # Example matrices B, C, D
        B = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

        C = [[9, 8, 7],
             [6, 5, 4],
             [3, 2, 1]]

        D = [[0, 1, 0],
             [1, 0, 1],
             [0, 1, 0]]

        A = add_matrices(add_matrices(B, C), D)

        # Display the result matrix A
        print("Matrix A (B + C + D):")
        for row in A:
            print(row)

    except MatrixSizeError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()