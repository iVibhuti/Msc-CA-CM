# Assignment 2: Calculate SVD of a 2 x 2 Symmetric matrix

## About the repository

### How to run the program

- Assuming that the executable for python 3 is set in PATH with the executable's name being `python`.
- One can run the program by using the command: `python main.py`.
- After ensuring both the test file and main file are in same directory, the test file can be run using: `python -m unittest -v main_test`

### Input Format

- Inputs are taken from a file, please provide full path to the file in order to run the program in relative or absolute format.
  - E.g.:

  ```shell
  Enter the name of the file to be opened: ./input.txt
  ```

### Output

- Output will be three different matrices in form of U, Wedge(∧) and U^-1 (U inverse).
  - E.g.:

  ```shell
  U:
  [[ 100  -50]
  [ -50 -100]]
  Wedge:
  [[-6.  0.]
  [ 0. -1.]]
  U^-1:
  [[ 0.008 -0.004]
  [-0.004 -0.008]]
  ```

## Author Information

- **Name:** Yash Dave
- **Github:** [Amorpheuz](https://github.com/amorpheuz)
- **PRN:** 19030142011
- **Batch:** MSc CA 2019-21 @ SICSR
