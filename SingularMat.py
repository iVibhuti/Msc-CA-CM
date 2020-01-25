def matrix(l):
    a = 0
    if len(l) == 1:
        return l[0][0]
    if len(l) == 2:
        b = l[0][0] * l[1][1] - l[0][1] * l[1][0]
        return b

    for i in range(len(l)):
        if len(l) > 1:
            mm = l[1:]
            mm = list(map(lambda x: x[:i] + x[i + 1:], mm))
            a += (-1) ** i * l[0][i] * matrix(mm)
        else:
            return a
    else:
        return a


if __name__ == '__main__':
    f = open('inputfile', 'r')
    l = [[int(num) for num in line.split(',')] for line in f]
    print(l)
    matrix(l)
    if matrix(l) == 0:
        print("Determinant of the Matrix:", matrix(l))
        print("Singular Matrix")
    else:
        print("Determinant of the Matrix:", matrix(l))
        print("Not Singular Matrix")