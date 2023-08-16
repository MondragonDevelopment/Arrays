# Find the smallest difference between elements of 2 given arrays

arrayA = [-1, 5, 10, 20, 28, 3]
arrayB = [26, 134, 135, 15, 17]


def smallestDifference(arr1, arr2):
    answer = []
    arr1.sort(), arr2.sort()
    minimum = 99999999999999
    first, second = 0, 0
    while first < len(arr1) and second < len(arr2):
        num1, num2 = arr1[first], arr2[second]
        if num1 == num2:
            answer[0], answer[1] = arr1[first], arr2[second]
            break
        elif num1 < num2:
            current = num2 - num1
            first += 1
        elif num1 > num2:
            current = num1 - num2
            second += 1
        else:
            return answer

        if current < minimum:
            minimum = current
            print(minimum)
            answer = [num1, num2]

    return answer


print(smallestDifference(arrayA, arrayB))
