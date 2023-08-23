array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

def longestPeak(array):
    lmax = 0
    for i in range(1, len(array) - 1, 1):
        print(i)
        if array[i - 1] < array[i] and array[i] > array[i + 1]:
            l, r = i - 2, i + 2
            while l >= 0 and array[l] < array[l+1]:
                l -= 1
            while r < len(array) and array[r] < array[r - 1]:
                r += 1
            lmax = max(lmax, r - l - 1)
            i += 2
        else:
            continue
    return lmax


print(longestPeak(array))