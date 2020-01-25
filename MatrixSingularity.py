#Pooja Naik
#PRN-19030142019
def matrix(l):
    det = 0
    if len(l)==2:
        det=(l[0][0] * l[1][1] - l[0][1] * l[1][0])
       # print("cofact's det",det)

    for i in range(len(l)):
        if(len(l)>1):
            cofact = l[1:]
            #print(cofact)
            cofact = list(map(lambda x: x[:i] + x[i + 1:], cofact))
            det += (-1)**i*l[0][i] * matrix(cofact)
        else:
            return det
    else:
        return det
if __name__=="__main__":
    f = open('inputfile', 'r')
    l = [[int(num) for num in line.split(',')] for line in f]
    print(l)
    matrix(l)
    if 0 == matrix(l):
        print("Final Determinant is:", matrix(l))
        print("True, The Matrix is Singular")
    else:
        print("Final Determinant is:", matrix(l))
        print("False, The matrix is Not Singular")

