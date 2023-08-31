"""
As a teacher, you have to reward your students based on the grades they recently got in a test.
- Each student must at least have one reward
- If a sudent's got a higher grade than the one next to them, they got to receive a strictly increasing reward
Return minimum number of rewards you are to give
def isMinimum(grades, i):
    if i == 0:
        return grades[i + 1] > grades[i]
    if i == len(grades) - 1:
        return grades[i - 1] > grades[i]
    return grades[i - 1] > grades[i] < grades[i + 1]


def isMaximum(grades, i):
    if i == 0:
        return grades[i + 1] < grades[i]
    if i == len(grades) - 1:
        return grades[i - 1] < grades[i]
    return grades[i - 1] < grades[i] > grades[i + 1]
"""


grades = [8,4,2,1,3,6,7,9,5]


def minRewards(grades):
    ind_rew = [1 for _ in grades] # This format is interesting
    for i in range(1, len(grades)):
        if grades[i] <= grades[i-1]:
            continue
        ind_rew[i] = ind_rew[i-1] + 1
    for i in range(len(grades) - 2, -1, -1):
        if grades[i] <= grades[i+1]:
            continue
        ind_rew[i] = max(ind_rew[i+1] + 1, ind_rew[i])

    return sum(ind_rew)


print(minRewards(grades))
