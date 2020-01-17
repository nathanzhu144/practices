def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size
                
    return dp[-1]

if __name__ == "__main__":
    lengthOfLIS([4, 10, 4, 3, 8, 9])