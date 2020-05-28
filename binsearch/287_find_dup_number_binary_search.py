# Nathan Zhu May 9th, 2020 1:02 am Second day of work at Salesforce is tomorrow.  Or today.
# Leetocode 287 | medium | not obvious lol
# Neither the O(N) or NlogN soln are obvious solutions.
# George asked me this question, and I didnt' see the binary search soln.  I like this one.


def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def helper(k):
        return len([num for num in nums if num <= k]) > k
    
    left, right, ret = 0, len(nums), -1
    while left <= right:
        mid = (right - left) // 2 + left
        if helper(mid):
            ret = mid
            right = mid - 1
        else: 
            left = mid + 1
    return ret