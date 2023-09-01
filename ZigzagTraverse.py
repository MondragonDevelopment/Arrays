"""
You are given a 2x2 array in a zigzag shape, return a 1D array with the numbers in that order
"""

array = [[1,3,4,10], [2,5,9,11], [6,8,12,15], [7,13,14,16]]


def zigzag(array):
    answer = []
    height, width = len(array) - 1, len(array[0]) - 1
    m, n = 0, 0
    goingDown = True
    while not outOfBounds(m, n, height, width):
        answer.append(array[n][m])
        if goingDown:
            if m == 0 or n == height:
                goingDown = False
                if n == height: # Since you are always going down, you first meet this condition
                    m += 1
                else:
                    n += 1
            else:
                n, m = n + 1, m - 1
        else:
            if n == 0 or m == width: # Since you are always going to the right, you first meet this condition
                goingDown = True
                if m == width:
                    n += 1
                else:
                    m += 1
            else:
                n, m = n - 1, m + 1
    return answer


def outOfBounds(m, n, height, width):
    return m <0 or m > width or n <0 or n >  height


print(zigzag(array))
