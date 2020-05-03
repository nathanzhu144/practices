# Nathan Zhu Saturday, April 26th, 2020, 12:18 am.  Stockton, CA 
# Leetcode 239 | medium | *DAMN SMART*
# Category: Monotonic queue (not used), DP presum (used)
# Presume category?
#
# Damn this one really got me.

# Suppose we have an array:
# [1, 3, -1, -3, 5, 3, 6, 7]
#
# We first split up each array into k-sized chunks, and calculate max value up to a point from
# left to right and right to left with respect to each k-sized chunk
#
# suppose k = 3
# left to right = [1, 3, 3   |  -3, 5, 5  |  6, 7]
#                  ------>       ------>     -->
# right to left = [3, 3, -1  |   5  5  3  |  7, 7]
#                  <------       <-----      <--
#
# Then, suppse we take a random subarray of size k, like [3, -1, -3]
# 
# left to right = [1, 3, 3   |  (-3), 5, 5  |  6, 7]
#                  ------>       ------>     -->
# right to left = [3, (3), -1  |   5  5  3  |  7, 7]
#                  <------       <-----      <--
# val[i] = max(right to left[i], left to right[i + k - 1])
# 
# 
# The value of this subarray is just max(3, -3).  We usually find maximum of an array by scanning 
# through left to right and finding the biggest element.  It is also correct to find the maximum
# of an array by SPLITTING AT A RANDOM POSITION, AND THEN LOOKING AT MAXIMUM FROM LEFT TO RIGHT AND RIGHT
# TO LEFT. 
#                    
# Ex. [3, 2, 3, 34, 23, 2, -1, 8, 2, 10]
#      <---------------    Start ---->
# We take maximum of two maximums to get max of while array.

def max_sliding_window(arr, k):
    N = len(arr)
    left_to_right, right_to_left = arr[:], arr[:]
    ret = []

    for i, num in enumerate(arr):
        if i % k == 0: continue
        else: left_to_right[i] = max(left_to_right[i - 1], num)

    for i in range(N - 1, -1, -1):
        if i % k == k - 1 or i == N - 1: continue
        else: right_to_left[i] = max(right_to_left[i + 1], arr[i])

    for i in range(N - k + 1):
        ret.append(max(right_to_left[i], left_to_right[i + k - 1]))
    return ret

    
if __name__ == "__main__":
    print(max_sliding_window([2, 2], 2))