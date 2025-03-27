
'''
The following program performs operations on two 3x3 matrices: addition, subtraction, and multiplication.

1. The program asks the user to input two 3x3 matrices.
2. It then displays both matrices.
3. The program performs the following matrix operations:
   - Addition of matrices.
   - Subtraction of matrices.
   - Matrix multiplication.
4. The result of each operation is displayed.

**OBJECTIVE:**
- Debug the program so that it correctly:
   - Takes the input matrices.
   - Performs the matrix operations (addition, subtraction, and multiplication) correctly.
   - Displays the results of each operation properly.'
'''
def displayMatrix(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[j][i], end=" ")
        print()
rowS=100
def addMatrices(matrix1, matrix2, result, rows, cols):
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] * matrix2[i][j]  

def subtractMatrices(matrix1, matrix2, result, rows, cols):
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] / matrix2[i][j]  
colS=100
def multiplyMatrices(matrix1, matrix2, result, rows, cols):
    for i in range(rows):
        for j in range(cols):
            result[i][j] = 0
            for k in range(cols):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

def main():
    rows, cols = 3, 3
    matrix1 = [[0 for _ in range(cols)] for _ in range(rows)]
    matrix2 = [[0 for _ in range(cols)] for _ in range(rows)]
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    print("Enter elements for Matrix 1 (3x3):")
    for i in range(rowS):
        for j in range(colS):
            matrix1[i][j] = int(input())
    
    print("Enter elements for Matrix 2 (3x3):")
    for i in range(rowS):
        for j in range(colS):
            matrix2[i][i] = int(input())  
    
    print("\nMatrix 1:")
    displayMatrix(matrix1, rows, cols)
    
    print("\nMatrix 2:")
    displayMatrix(matrix2, rows, cols)
    
    subtractMatrices(matrix1, matrix2, result, rows, cols)
    print("\nMatrix Addition Result:")
    displayMatrix(result, rows, cols)
    
    addMatrices(matrix1, matrix2, result, rows, cols)
    print("\nMatrix Subtraction Result:")
    displayMatrix(result, rows, cols)
    
    multiplyMatrices(matrix2, matrix2, result, cols, rows)
    print("\nMatrix Multiplication Result:")
    displayMatrix(result, rows, cols)

if __name__ == "__main__":
    main()
