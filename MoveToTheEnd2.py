# Move target element of an array to the end of it (solved with two pointers)
# O(N) time | O(1) Space

array = [2,1,2,2,2,3,4,2]
tar = 2

def moveEnd(array, target):
    l, r = 0, len(array) - 1
    while l < r:
        if array[r] != target and array[l] == target:
            array[l] = array[r]
            array[r] = target
            l, r = l + 1, r - 1
        elif array[l] != target:
            l += 1
        elif array[r] == target:
            r -= 1
    return array


print(moveEnd(array, tar))
