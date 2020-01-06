def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if not nums: return []
    N = len(nums)
    idx = 0
    ret = list()

    while idx < N:
        # we want to find the start, end of each summary range
        start, end = idx, idx
        while end < N - 1 and nums[end + 1] == nums[end] + 1:
            end += 1
            
        # depending if start and end are different numbers, we append different nums
        if end > start: ret.append(str(nums[start]) + "->" + str(nums[end]))
        else: ret.append(str(nums[start]))
            
        # starting index moves to end of last interval + 1
        idx = end + 1

    return ret