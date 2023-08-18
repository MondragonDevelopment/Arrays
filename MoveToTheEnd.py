# Move target element of an array to the end of it
# O(N) time | O(N) Space

array = [2,1,2,2,2,3,4,2]
tar = 2

def moveEnd(array, target):
    n = 0
    answer = []
    for i in range(len(array)):
        if array[i] == target:
            n+=1
        else:
            answer.append(array[i])
    answer.extend([tar]*n)
    return answer


print(moveEnd(array, tar))
