# Determine if the given array has a monotonic behaviour
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

def monotonicArray(array):
    for i in range(1, len(array), 1):
        if array[i-1] == array[i]:
            continue
        elif array[i-1] < array[i]:
            while i < len(array) and array[i-1] <= array[i]: # Expression is evaluated from left to right
                i += 1
            if i == len(array): return True
            else: return False
        elif array[i-1] > array[i]:
            while i < len(array) and array[i-1] >= array[i]:
                i += 1
            if i == len(array): return True
            else: return False

        return


print(monotonicArray(array))
