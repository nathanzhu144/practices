# Nathan Zhu May 16th, 2020.  5:46 pm, Broke top 200 last week, got exactly 188 briefly, but went down to position 400 because I had 4 stupid mistakes. 
# Leetocde 1402 | hard | damn pretty hard
# Category: DP / Greedy
# There is a N^2 dp soln, but this is an O(N) greedy.
# Can be done in O(1) space, but done here in O(N) space.
# Similar to nested weight sum II

def maxSatisfaction(arr):
    """
    :type satisfaction: List[int]
    :rtype: int
    """
    # How does this work?
    # 1. We sort array from biggest to smallest.
    #
    # 2. We get the presum array of the array from left to right
    #
    # 3. We do a pre-sum on the pre-sum array to get the right weightings.
    #
    # 4. we return max of array and 0.
    #
    # Think about what a prefix array represents, 
    #     prefix arr:                 [0,  0 + 1,  0 + 1 + 2, 0 + 1 + 2 + 3, 0 + 1 + 2 + 3 + 4]
    #     prefix arr of prefix arr    [0, 2 * 0 + 1, 3 * 0 + 2 * 1 + 1 * 2, 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3, ... ]
    #                                 As we go thru, we can get the appropriate weightings of each element, as everytime
    #                                 we add our prefix sum, we add another copy of all the weights we have seen so far.
    #                                 
    #
    # Ex. [-9, -8, -1, 0,   5]   sorted add
    #     [ 5,  5  4, -4, -13]    prefix sum
    #     [5,  10, 14,11,  -2]    prefix sum of prefix sum
    #
    # Return 14. 
    #
    # WE can also do this in O(1) space, but I felt that this was a clearer illustration.
    # 
    N = len(arr)
    arr.sort(reverse=True)
    for i in range(1, N): arr[i] += arr[i - 1]
    for i in range(1, N): arr[i] += arr[i - 1]
        
    return max(0, max(arr))  # return 0 instead of negative, if we can't get a positive.
        