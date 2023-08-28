"""
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order,
then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.
"""
nums = [2,6,4,8,10,9,15]
nums2 = [2,1]
nums3 = [1,3,2,4,5]
nums4 = [1,3,2,3,3]

def findUnsortedSubarray(nums):
    minunsort = float("inf")
    maxunsort = float("-inf")
    for i in range(len(nums)):
        num = nums[i]
        if isOutOfOrder(i, num, nums):
            minunsort = min(minunsort, num)
            maxunsort = max(maxunsort, num)
    if minunsort == float("inf"):
        return 0
    subl, subr = 0, len(nums) - 1
    while minunsort >= nums[subl]: # This one finds the index of the leftmost unsorted number, i.e., the maxunsort position by ignoring numbers less than or equal to minunsort
        subl += 1
    while maxunsort <= nums[subr]: # Same as last while loop but inverted
        subr -= 1
    answer = subr - subl + 1 # since subr is the position of minunsort, we need to add 1 to get the real length between both unsorted numbers' position
    return answer


def isOutOfOrder(i, num, array):
    if i == 0:
        return  num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]


print(findUnsortedSubarray(nums2))
print(findUnsortedSubarray(nums))
print(findUnsortedSubarray(nums3))
print(findUnsortedSubarray(nums4))
