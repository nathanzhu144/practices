# Nathan Zhu April 10th, 2020 Contest.
# Leetcode 1441 | easy | easy
# Category: fizzbuzz

def buildArray(target, n):
    """
    :type target: List[int]
    :type n: int
    :rtype: List[str]
    """
    ret = []
    curr = 1
    for num in target:
        while curr != num:
            ret.append("Push")
            ret.append("Pop")
            curr += 1
        else:
            curr += 1
        ret.append("Push")
    return ret
            