# Nathan Zhu January 17th, 2019 4:15 pm Duderstadt Interview Area 
# Leetcode 179 | medium | medium?
# Category: Sorts
# 
# The idea here is pretty simple, and we leverage string comparison.
# While there are a lot of edge cases with numbers, since we will concatenate all the numbers
# together in the end, one easy way to get the max number is to try contating x + y, y + x and seeing 
# which one is bigger.

# Since python's sort is usually a min sort, we do reverse=True


def largestNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    nums = map(str, nums)
    nums.sort(cmp = lambda a, b: cmp(a + b, b + a), reverse=True)
    return "".join(nums).lstrip('0') or '0'