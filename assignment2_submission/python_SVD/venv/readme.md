#S_V_D

The svd file calculates UΣV^T for the 2*2 matrix
 -input.txt is a file which provides the input to the S_V_d
 -test.py is a file which has the test cases to check the      function of S_v_d


Content of S_v_d
 there are basically three function which are design to calculte the for 
 -eigenvalue : takes input as a 2*2 matrix and returns the two eigen values also checks the value of 'd' if it  is 0 it gives a proper message for the same  calulates the rrot of equation by formula -b +- root of b^2 - 4ac / 2a
  -inverse : takes input as 2*2 matrix and returns the inverse of the matrix and also calculates the determinent for the inverse.
  -eigenvector : take eigen value and the two roots of equation as a input and returns the eigen value as the output

Content of input.txt
 -it just gives 2*2 matrix as the input for the calculation of S_v_d to main file

Content of test.py
-contains the test cases to check the function define in the main file
