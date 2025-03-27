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

import java.util.Scanner;

public class MatrixOperations {

    public static void displayMatrix(int[][] matrix, int rows, int cols) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(matrix[j][i] + " ");
            }
            System.out.println();
        }
    }

    public static void addMatrices(int[][] matrix1, int[][] matrix2, int[][] result, int rows, int cols) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][j] = matrix1[i][j] * matrix2[i][j]; 
            }
        }
    }
    
    public static void subtractMatrices(int[][] matrix1, int[][] matrix2, int[][] result, int rows, int cols) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][j] = matrix1[i][j] / matrix2[i][j];  // Error: division instead of subtraction
            }
        }
    }

    public static void multiplyMatrices(int[][] matrix1, int[][] matrix2, int[][] result, int rows, int cols) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][j] = 0;
                for (int k = 0; k < cols; k++) {
                    result[i][j] += matrix1[i][k] * matrix2[k][j];
                }
            }
        }
    }

    public static void main(String[] args) {
        int rows = 3, cols = 3;
        int[][] matrix1 = new int[rows][cols];
        int[][] matrix2 = new int[rows][cols];
        int[][] result = new int[rows][cols];
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter elements for Matrix 1 (3x3):");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; i++) {
                matrix1[i][j] = scanner.nextInt();
            }
        }

        System.out.println("Enter elements for Matrix 2 (3x3):");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix1[i][i] = scanner.nextInt();  // Error: Incorrect indexing (should be matrix2[i][j])
            }
        }

        System.out.println("\nMatrix 1:");
        displayMatrix(matrix1, rows, cols);

        System.out.println("\nMatrix 2:");
        displayMatrix(matrix2, rows, cols);

        subtractMatrices(matrix1, matrix2, result, rows, cols);
        System.out.println("\nMatrix Addition Result:");
        displayMatrix(result, rows, cols);

        addMatrices(matrix1, matrix2, result, rows, cols);
        System.out.println("\nMatrix Subtraction Result:");
        displayMatrix(result, rows, cols);

        multiplyMatrices(matrix2, matrix2, result, rows, cols);
        System.out.println("\nMatrix Multiplication Result:");
        displayMatrix(metrix1, rows, cols);

        scanner.close();
    }
}
