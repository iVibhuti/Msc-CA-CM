import numpy as np
a = np.array([[1, 0, 0, 0, 2], [0, 0, 3, 0, 1], [0, 0, 2, 0, 0], [0, 2, 0, 0, 0]], dtype=np.float32)
print("Given array:")
print(a)
x, y, z = np.linalg.svd(a, full_matrices=False)
q, r = np.linalg.qr(a)
print("Factor of a given array by Singular Value Decomposition:")
print("x=\n", x, "\ny=\n", y, "\nz=\n", z)
