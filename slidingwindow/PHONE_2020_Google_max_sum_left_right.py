# Nathan Zhu Jan 25th, 2019 10:31 am, Ugli 3rd floor
# Google phone question | medium | damn this is a good question
# Category: Sliding window / DP
# Runtime: O(N)
# 
# Find the maximum sum possible by adding numbers in list together. You can EXACTLY k numbers,
# must select from left or right side of the subarray (like a queue)
# https://leetcode.com/discuss/interview-question/441495/Google-or-Phone-or-Max-Sum-from-left-or-right/397371
# 
# Naively, this seems like a DP problem, where you memoize on 3 things:
# i, j where i, j represent a subarray and k, where k is the number of choices you have left.
# 
# we actually don't need k, as to get to any (i, j), we would have the same k every time.
#
# Furthermore, as we can ONLY remove from left or right, we can rephrase this question as finding 
# the smallest contiguous subarray sum of size N - K.


def solve(arr, k):
    minsubarr = float('inf')
    N = len(arr)
    left, right = 0, 0
    presum = 0

    while right < N:
        presum += arr[right]
        right += 1
        
        if right - left == N - k:
            minsubarr = min(minsubarr, presum)
            presum -= arr[left]
            left += 1

    return sum(arr) - minsubarr

if __name__ == "__main__":
    print(solve([2, 3, 5, 7, 1], 3))
    print(solve([5, 10, 2, 9, 11], 3))
