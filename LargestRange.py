"""
Given an unsorted array of integers nums, return the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""
arr = [1,11,3,0,15,5,2,4,10,7,12,6]
nums = [0,3,7,2,5,8,4,6,0,1]


def largestRange(nums):
    isExplorable = {}
    longest = []
    lenolon = 0
    half = len(nums)//2
    for num in nums:
        isExplorable[num] = True
    for num in nums:
        if lenolon > half:
            return longest
        if not isExplorable[num]:
            continue
        isExplorable[num] = False
        curr = 1
        prev = num - 1
        pos = num + 1
        while prev in isExplorable:
            isExplorable[prev] = False
            curr += 1
            prev -= 1
        while pos in isExplorable:
            isExplorable[pos] = False
            curr += 1
            pos += 1
        if curr > lenolon:
            lenolon = curr
            longest = [prev + 1, pos - 1]
    return longest


print(largestRange(arr))
print(largestRange(nums))
