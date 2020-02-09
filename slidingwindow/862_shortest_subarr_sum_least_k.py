# Nathan Zhu Jan 20th, 2020 2nd floor of potbelly, near back, State Street.  The wifi up here is bad, but leetcode don't need good wifi.
# Leetcode 862 | hard | pretty damn hard, if you don't think of using a monotonic array
# Category: Sliding window
# Note: I was thinking about it, and I think a queue is not necessary if you keep track of the front of the array
#       with an index.
# 

import collections

# So, the normal shortest subarray of sum K has only positives, so it is pretty easy
# The *reason* sliding window works on that one is simple:
# 
# Suppose we have an subarray starting at idx START, and ending at idx, END
# 
# 1. If [START, END] does not have subarray K, [START + 1, END] also doees not have subarray K
# 2. If [START, END] has subarray K, [START + 1, END], may have subarray K.
#
# However, when we introduce negatives, assumption 1 becomes false.  Therefore, we decide to use a monotonic queue,
# which stores only numbers in increasing order.  
# 
# The first while loop makes sense, for most people.
#
# How about the second one?  

def shortestSubarray(A, K):
    d = collections.deque([[-1, 0]])   # d is a deque of [idx, presum int], and is monotonically increasing by presum int
                                        # Though, idx is also monotonically increasing (but that's not important)
    ret, curr = float('inf'), 0
    for i, num in enumerate(A):
        curr += num
        while d and curr - d[0][1] >= K:
            ret = min(i - d.popleft()[0], ret)
        # Invariants at this point in code: curr - d[0][1] < K or d is empty.
        #             Consider: [1, 1, 1, -2, 2], target = 3 right before idx == 3 is considered
        #                idx     0  1  2   3  4
        #                                Here
        # 
        #          q =  [-1, 0], [0, 1], [1, 2], [2, 3]
        #          curr was 3, now is 1.
        # 
        #          In the previous while loop, we should've stored that [1, 1, 1] makes 3, so it is fine if we don't come back to this.
        #          As the presum goes to 1, to preserve a monotonically increasing array, we pop off the end until we get to a value of 1.
        while d and curr <= d[-1][1]:
            d.pop()
        d.append([i, curr])
            
    return ret if ret != float('inf') else -1


if __name__ == "__main__":
    print(shortestSubarray([1, 1, 1, 1, 1, 1, -3, 1, 1,], 6))
    print(shortestSubarray([5, -4, 2, 3, 4], 6))