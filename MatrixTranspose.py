def findMatrixTranspose(matrix, length):
    for i in range(length):
        for j in range(len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


if __name__ == "__main__":
    noOfRows = int(input("Enter the no.of rows : "))

    matrix = []
    for i in range(noOfRows):
        matrix.append(list(map(int, input().strip('[').strip(']').split(','))))

    print(findMatrixTranspose(matrix, noOfRows))
