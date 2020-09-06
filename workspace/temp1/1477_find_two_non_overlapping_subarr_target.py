# /* Nathan Zhu June 13th, 2020  
# *  Leetcode 1477 | medium | hard
# *  Category: sliding window O(N)
#  Damn nobody else did this soln.  I don't even know if I understand this soln, but this soln relies on
#  insights from sliding window + maximum profit with two trades
#
#  One insight is that length of shortest array adding up to k monotonically dereases, as we move left to right
#  and if we move right to left.
#
#  This is larr and rarr.
#
#  Then, we use maximum profit with two trades to get minimum length of two.
#
#  Can't believe I thought of this soln
# */



def minSumOfLengths(arr, target):
    """
    :type arr: List[int]
    :type target: int
    :rtype: int
    """
    N = len(arr)
    left, right, currsum = 0, 0, 0
    larr = [float('inf') for i in range(N)]
    rarr = [float('inf') for i in range(N)]

    while right < N:
        currsum += arr[right]
        right += 1
        while left <= right and currsum >= target:
            if currsum == target:
                if rarr[left] == float('inf'): rarr[left] = right - left
                larr[right - 1] = right - left
            currsum -= arr[left]
            left += 1

    # larr now is "smallest" subarray == k ending at index i (inclusive)
    # rarr now is "smallest" subarray == k starting at index i (inclusive)

    for i in range(1, N):
        larr[i] = min(larr[i - 1], larr[i])

    for i in range(N - 2, -1, -1):
        rarr[i] = min(rarr[i + 1], rarr[i])

    ret = float('inf')
    for i in range(1, N):
        ret = min(ret, larr[i - 1] + rarr[i])
    return -1 if ret == float('inf') else ret
