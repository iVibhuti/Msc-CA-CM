# Assignment 1: Determine if a matrix is singular or not
## About the repository
### How to run the program?
- Assuming that the executable for python 3 is set in PATH with the executable's name being `python`.
- One can run the program by using the command: `python main.py`.
- After ensuring both the test file and main file are in same directory, the test file can be run using: `python -m unittest -v main_test`
### Input Format
- Inputs are given by the user via the CLI.
- The program will first ask the user for the number of rows and columns in the matrix, since only square matrices can have an inverse. Provide appropriate input in form of a number.
    - Example: 
    ```c
    Enter number of rows & cols in square matrix: 3
    ```
- Inputs should be given row by row, with each value of a column seperated by a `whitespace`.
    - Example input for a 3x3 matrix: 
    ```c
    Enter values in row 1 separated by spaces: 1 2 3
    Enter values in row 2 separated by spaces: 4 5 6
    Enter values in row 3 separated by spaces: 7 8 9
    ```
- The program will print a representation of the input matrix once all the input is given.
    - Sample output for the matrix in the example above:
    ```
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ```
### Output
The output will show the value of the determinant and based upon it, the singularity/non-singularity of a matrix.
Example output:
```
Determinant: -2
Matrix is Non-Singular
```

## Author Information
- **Name:** Yash Dave
- **Github:** [Amorpheuz](https://github.com/amorpheuz)
- **PRN:** 19030142011
- **Batch:** MSc CA 2019-21 @ SICSR