def det(mat, count=0):
    index = list(range(len(mat)))

    if len(mat) == 2 and len(mat[0]) == 2:
        val = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return val

    for col in index:
        second = mat.copy()
        second = second[1:]
        row = len(second)

        for i in range(row):
            second[i] = second[i][0:col] + second[i][col + 1:]

        notation = (-1) ** (col % 2)  # F)

        sub_det = det(second)

        count += notation * mat[0][col] * sub_det

    return count


def singular(matrix):
    if det(matrix) == 0:
        print("is singular")
        return True
    else:
        print("it is not a singular matrix")
        return False

