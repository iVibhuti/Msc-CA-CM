"""Name:Edna Martis
PRN:19030142015"""


def matrix(l):
    d = 0
    if len(l) == 1:
        return l[0][0]
    if len(l) == 2:
        m = l[0][0] * l[1][1] - l[0][1] * l[1][0]
        return m

    for i in range(len(l)):
        if len(l) > 1:
            cf = l[1:]
            cf = list(map(lambda x: x[:i] + x[i + 1:], cf))
            d += (-1) ** i * l[0][i] * matrix(cf)
        else:
            return d
    else:
        return d


if __name__ == '__main__':
    f = open('inputfile', 'r')
    l = [[int(num) for num in line.split(',')] for line in f]
    print(l)
    matrix(l)
    if matrix(l) == 0:
        print("Determinant of the Matrix:", matrix(l))
        print("Singular")
    else:
        print("Determinant of the Matrix:", matrix(l))
        print("Not Singular")
