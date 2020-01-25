# Determine if a matrix is singular or non-singular

This is the Assignment-1 of Computational Methods to determine if a given matrix is singular or non-singular. Also to create the test cases for the same.

## Prerequisites

* Python 3.7 or above should be installed with PATH set.
* IDE or Text Editor you like the best.

## Running the program

* Open the terminal or command prompt.
* Go to directory where the python file is saved.
* Run the program by using the command: 
```
python singularMatrix.py
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
  python -m unittest -v test_singularMatrix.py
  ```
  * Or, run the tests normally:
  ```
  python -m unittest test_singularMatrix.py
  ```

## Input Format
 
* Inputs are given by a simple text file: `matrix.txt`.
* Each character in a file is seperated by tab space or single space. For example:
```
1 2 3
4 5 6
3 2 1
```

## Output

* The output will show `Matrix is Singular` OR `Matrix is Non-Singular` based upon the determinant calculated for a given matrix.

## Built With

* [Pyhton 3.7](https://www.python.org/downloads/release/python-370/) - Programming Language
* [PyCharm Professional](https://www.jetbrains.com/pycharm/) - IDE for Python

## Author

* [**Sahajkumar Lad**](https://github.com/ladsahaj) - *19030142027*
* MSc[CA] (2019-21) @SICSR 


## Acknowledgments

* [Python unittest](https://docs.python.org/3/library/unittest.html)
