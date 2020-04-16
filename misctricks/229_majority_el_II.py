# Nathan Zhu Feb 16th, 2020.  Day after birthday, beem studying 376 today, reached like level 4k in gemcraft, good day.
#                             Talked to Ellen about 376 too.  She doesn't get reductions too well.
# Leetcode 229 | medium | hard to prove
# Category: Misc tricks


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums: return []
    c1, c2, num1, num2 = 0, 0, 0, 1
    for num in nums:
        if num == num1: c1 += 1
        elif num == num2: c2 += 1
        elif c1 == 0:
            c1 = 1
            num1 = num
        elif c2 == 0:
            c2 = 1
            num2 = num
        else:
            c1 -= 1
            c2 -= 1
            
    return [n for n in [num1, num2] if nums.count(n) > len(nums) // 3]