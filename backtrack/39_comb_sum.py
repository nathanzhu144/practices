# Nathan Zhu Jan 5th, 2020 12:49 pm SI 106, we have an exam tomorrow
# Leetcode 39 | medium | not bad
# Category: backtracking


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ret = []
    def helper(i, currpath, currsum):
        if currsum > target: return
        if i == len(candidates):
            if currsum == target: ret.append(currpath[:])
            return
        helper(i, currpath + [candidates[i]], currsum + candidates[i])
        helper(i + 1, currpath, currsum)
        
    helper(0, [], 0)
    return ret