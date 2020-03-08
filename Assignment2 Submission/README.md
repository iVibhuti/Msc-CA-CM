# Compute the factor of a given matrix by Singular Value Decomposition

This is the Assignment-2 of Computational Methods to compute the EigenValues, EigenVectors, U, carret(^) and inverse of U of a 2X2 Matrix by using Singular Value Decomposition. Also to create the test cases for the same.

## Prerequisites

* Python 3.7 or above should be installed with PATH set.
* IDE or Text Editor you like the best.

## Running the program

* Open the terminal or command prompt.
* Go to directory where the python file is saved.
* Run the program by using the command: 
```
python singularValueDecomposition.py
```
* The program will ask to enter the file name. Enter the full path and file name with its extension.
```
Enter the file name with path : C:\Users\....\matrix.txt
```

## Running the tests

* Open the terminal or command prompt.
* Go to directory where the python file is saved.
* Ensure that test file and main file are in the same directory.
* Run the test file by using one of the command below:
  
  * Run tests with more detail (higher verbosity) by passing in the -v flag:
  ```
  python -m unittest -v test_singularValueDecomposition.py
  ```
  * Or, run the tests normally:
  ```
  python -m unittest test_singularValueDecomposition.py
  ```

## Input Format
 
* Inputs are given by a simple text file: `matrix.txt`.
* It should be 2X2 Matrix (2 rows and 2 columns).
* Each character in a file is seperated by tab space or single space. For example:
```
1 -1
-1 1
```

## Output

* The output will show EigenValues, U, caret(^) and inverse of U for a given matrix. For example:
```
Eigen Values : [2.0, 0.0]
U : 
[-1.0, 1.0]
[1.0, 1.0]
Caret(^) : 
[2.0, 0.0]
[0.0, 0.0]
Inverse of U : 
[-0.5, 0.5]
[0.5, 0.5]
```

## Built With

* [Pyhton 3.7](https://www.python.org/downloads/release/python-370/) - Programming Language
* [PyCharm Professional](https://www.jetbrains.com/pycharm/) - IDE for Python

## Author

* [**Sahajkumar Lad**](https://github.com/ladsahaj) - *19030142027*
* MSc[CA] (2019-21) @SICSR 


## Acknowledgments

* [Python unittest](https://docs.python.org/3/library/unittest.html)
* [Linear Algebra](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)
