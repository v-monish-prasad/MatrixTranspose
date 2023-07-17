def findMatrixTranspose(matrix, noOfRows):
    noOfColumns = len(matrix[0])
    transpose = [[0 for i in range(noOfRows)] for j in range(noOfColumns)]

    for i in range(noOfRows):
        for j in range(noOfColumns):
            transpose[j][i] = matrix[i][j]

    return transpose


if __name__ == "__main__":
    noOfRows = int(input("Enter the no.of rows : "))

    matrix = []
    for i in range(noOfRows):
        matrix.append(list(map(int, input().strip('[').strip(']').split(','))))

    print(findMatrixTranspose(matrix, noOfRows))
