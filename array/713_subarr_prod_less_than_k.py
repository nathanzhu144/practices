# Nathan Zhu September 13th, 2019 11:47 am, 3 days before career fair.
# Leetcode 713 | medium | medium
# Category: Sliding window.


def num_subarr_prod_less_k(arr, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if not arr: return 0

    currprod = 1
    left, right, ret = 0, 0, 0

    while right < len(arr):
        currprod *= arr[right]

        # We NEED all 3 conditions
        # left has to stay in bounds (right isn't always in bounds)
        while left < len(arr) and left <= right and currprod >= k:
            currprod /= arr[left]
            left += 1
        ret += right - left + 1
        
        right += 1
        
    return ret
    #return ret if ret >= 0 else 0

if __name__ == "__main__":
    print(num_subarr_prod_less_k([1, 2, 3], 0))