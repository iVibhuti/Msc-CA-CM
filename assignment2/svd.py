import matrix.mat_operations as matop
# Singular value decompostion of 2x2 matrix

# Reading input from file
matrix = matop.read_csv("input_matrix.csv")
m1, m2 = matrix[0]
m3, m4 = matrix[1]

e1 = ((m1+m2) + ((m1-m4)**2 + 4*m2*m3)**0.5)/2
e2 = ((m1+m2) - ((m1-m4)**2 + 4*m2*m3)**0.5)/2

evalue_matrix = [[e1, 0], [0, e2]]
evector_matrix = []
e = e1
x = m2
y = e-m1
r = (x*x+y*y)**0.5
if r > 0:
     x /= r
     y /= r
else:
    x = e-m4
    y = m3
    r = (x*x+y*y)**0.5
    if r > 0:
         x /= r
         y /= r
    else:
        x = 1
        y = 0
evector_matrix.append([x,y])

e = e2
x = m2
y = e-m1
r = (x*x+y*y)**0.5
if r > 0:
     x /= r
     y /= r
else:
    x = e-m4
    y = m3
    r = (x*x+y*y)**0.5
    if r > 0:
         x /= r
         y /= r
    else:
        x = 1
        y = 0
evector_matrix.append([x, y])
print(evector_matrix, evalue_matrix, matop.inverse_mat(evector_matrix))