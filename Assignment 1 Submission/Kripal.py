
global N 
N = 1
def cofactor(mat,temp,p,q,n): 
	i = 0
	j = 0
	for row in range(n): 
		for col in range(n): 
			if (row != p and col != q): 
				temp[i][j] = mat[row][col] 
				j += 1
				if (j == n - 1): 
					j = 0
					i += 1
def single(mat,n): 
	D = 0 
	if (n == 1): 
		return mat[0][0] 
	temp = [[0 for i in range(N + 1)] for i in range(N + 1)]
	sign = 1 
	for f in range(n):  
		cofactor(mat, temp, 0, f, n) 
		D += sign * mat[0][f] * single(temp, n - 1) 
		sign = -sign 
	return D
if __name__ == '__main__':
        mat = [[4, 10, 1],[0, 0, 0],[1, 4, -3]]
        if (single(mat, N)):
            print("Matrix is Singular")
        else:
            print("Matrix is non-singular") 




