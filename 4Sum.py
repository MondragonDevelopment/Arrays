"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""
nums = [1,0,-1,0,-2,2]
nums2 = [-5,5,4,-3,0,0,4,-2]
target = 0


def fourSum(nums, target):
    pairSums = {}
    answer = []
    for i in range(1, len(nums) - 1):
        for j in range(i+1, len(nums)):
            curr = nums[i] + nums[j]
            diff = target - curr
            if diff in pairSums:
                for pair in pairSums[diff]:
                    answer.append(pair + [nums[i], nums[j]])
        for k in range(0, i):
            curr = nums[i] + nums[k]
            if curr not in pairSums:
                pairSums[curr] = [[nums[i], nums[k]]]
            else:
                pairSums[curr].append([nums[i], nums[k]])
    return answer


print(fourSum(nums2, target))
