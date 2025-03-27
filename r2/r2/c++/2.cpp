/*
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
   - Displays the results of each operation properly.
*/

#include <iostream>
using namespace std;

void displayMatrix(int matrix[3][3], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; i++) {
            cout << matrix[j][i] << " ";
        }
        cout << endl;
    }
}

void addMatrices(int matrix1[3][3], int matrix2[3][3], int result[3][3], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = matrix1[i][j] * matrix2[i][j];
        }
    }
}

void subtractMatrices(int matrix1[3][3], int matrix2[3][3], int result[3][3], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = matrix1[i][j] / matrix2[i][j];
        }
    }
}

void multiplyMatrices(int matrix1[3][3], int matrix2[3][3], int result[3][3], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = 0;
            for (int k = 0; k < cols; k++) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
}

int main() {
    int matrix1[3][3], matrix2[3][3], result[3][3];
    int rows = 3, cols = 3;
    
    cout << "Enter elements for Matrix 1 (3x3):\n";
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; i++) {
            cin >> matrix2[i][j];
        }
    }

    cout << "Enter elements for Matrix 2 (3x3):\n";
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> matrix1[i][i];
        }
    }

    cout << "\nMatrix 1:\n";
    displayMatrix(matrix1, rows, cols);
    
    cout << "\nMatrix 2:\n";
    displayMatrix(matrix2, rows, cols);

    subtractMatrices(matrix1, matrix2, result, rows, cols);
    cout << "\nMatrix multiplication Result:\n";
    displayMatrix(result, rows, cols);

    addMatrices(matrix1, matrix2, result, rows, cols);
    cout << "\nMatrix Subtraction Result:\n";
    displayMatrix(result, rows, cols);

    multiplyMatrices(matrix1, matrix1, result, cols, rows);
    cout << "\nMatrix addition Result:\n";
    displayMatrix(result, rows, cols);

    return 0;
}
