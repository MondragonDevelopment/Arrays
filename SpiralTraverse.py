# Given a 2D array, writet a functtttion that returns a 1D array with every element in spiral order

array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def spiralTraverse(array):
    xMin, xMax = 0, len(array)
    yMin, yMax = 0, len(array[0])
    x, y = 0, 0
    answer = []
    while xMin < xMax and yMin < yMax:
        if x == xMin and y == yMin:
            for y in range(yMin, yMax, 1):
                answer.append(array[x][y])
            x, xMin = x + 1, xMin + 1
        if y == yMax - 1 and x == xMin:
            for x in range(xMin, xMax, 1):
                answer.append(array[x][y])
            y, yMax = y - 1, yMax - 1
        if x == xMax - 1 and y == yMax - 1:
            for y in range(yMax - 1, yMin - 1, -1):
                answer.append(array[x][y])
            x, xMax = x - 1, xMax - 1
        if y == yMin and x == xMax - 1:
            for x in range(xMax - 1, xMin - 1, -1):
                answer.append(array[x][y])
            y, yMin = y + 1, yMin + 1
    print(x, y)
    return answer


# print(spiralTraverse(array))
print(spiralTraverse(matrix))
