# Nathan Zhu July 18th, 2019 9:22 pm 55 John Street
# 
# The first thing to realize is that in the general case, search insert position is
# a classic case of finding the smallest number bigger or equal to a number. Cause,
# the position of that number is the insert position.
#

# Why is THIS line important? Suppose we search for a integer that is 
# BIGGER than any other element in the array, if arr[mid] > target: will
# never run. ret will never get assigned to.  Therefore, if we intend ret
# to NOT return -1 when we do not find the element, and we intend for it to
# return the insert position, we should set ret to len(arr) in the beginning.
#
# Standard lower bound binary search, with a (small) catch
def search_insert(arr, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(arr) - 1
    ret = len(arr)                   # THIS line is IMPORTANT,
    while left <= right:
        mid = (right - left) // 2 + left
        if arr[mid] == target: return mid
        if arr[mid] > target:
            ret = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return ret