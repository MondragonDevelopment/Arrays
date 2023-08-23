array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]


def longestPeak(array):
    lmax = 0
    i = 1
    while i < len(array) - 1:
        print(i)
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        l, r = i - 2, i + 2 # l is left index, r is right index
        while l >= 0 and array[l] < array[l+1]:
            l -= 1
        while r < len(array) and array[r] < array[r - 1]:
            r += 1
        lmax = max(lmax, r - l - 1)
        i = r
    return lmax


print(longestPeak(array))
