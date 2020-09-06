
# /* Nathan Zhu Thursday July 23rd, 2020 5:30 pm Stockton, CA.  Rak joined leetcode group yesterday.  Also, watching kissing booth 2 tomorro apparently.
# *  Leetcode 1347 | hard | definitely hard
# *  Category: math, going backwards
# */

import heapq

# How to get from iteration k to iteration k + 1?
# [1, 3, 5]   # Iteration k
# [9, 3, 5]   # Iteration k + 1

# On iteration k + 1, we look at the largest number 9.  Obviously, 
# taking 9 and subtracting the other numbers would give us the original
# value of 9.

# 9 - (3 + 5) = 1                             (like this)

# However, this would require us to find the sum of the other numbers in the array
# This takes O(N) time per iteration.
# We can also do this.

# 9 - ((sum whole array) - 9) =
# 9 - ((9 + 3 + 5) - 9) = 9 - (3 + 5) = 1

# The advantage of this approach is we can update the new sum whole array in O(1)
# time.

# Ex of invalid array.
# [8, 5]     # 8 - (13 - 8) = 8 - 5 = 3
# [3, 5]     # 5 - (8 - 5) = 5 - 3 = 2
# [3, 2]     # 3 - (5 - 3) = 3 - 2 = 1
# [1, 2]     # 2 - (3 - 2) = 2 - 1 = 1
# [1, 1]

# Edge case: 
# Case 1
# [9, 9, 9]  
# 9 - (27 - 9) == -9 ???
# Caught by while loop greater check.
#
# Case 2:
# [5, 50] 
# 50 - (55 - 50) = 5    [5, 5]
# 5 - (10 - 5) = 0      [5, 0]
# 5 - (5 - 5) = 5
# 5 - (5 - 5) = 5       ...
# With a modulus there's a runtime error.
#
#
# Case 3:
# A 2-length array with 1 as one of the numbers, and the other as a positive integer should always be true.
# Like [1, A], [A, 1] where A is positive.
#
# 5, 1   =  5  -   ( 6 - 5) = 4
# 4, 1   =  4  -   ( 5 - 4) = 3
# 3, 1   =  3  -   ( 4 - 3 ) = 2
# 2, 1   =  2  -   ( 3 - 2) = 1   => [1, 1] return true.
# STOP
#     #print(isPossible([2,900000002]))
# If we do not do the modulus, we should stop at the correct step and return true.
#
# However, doing this:
# 5, 1   = 5 % (6 - 5) = 5 % 1 == 0  => [0, 1] ??? return false.
# We totally skip over the last step, returning false.
#    
# I'm actually pretty certain that 

def isPossible(target):
    """
    :type target: List[int]
    :rtype: bool
    """
    tot = sum(target)
    N = len(target)
    pq = [-num for num in target]   # python is default min queue, we want max q, so invert all nums
    heapq.heapify(pq)               # heapifies in O(N)
    
    # First check is whether sum of numbers is greater than N
    # Second check is for edge case 2.  Intuitively, sum of all previous numbers should be greater than half of current array.
    # Second check catches edge case 1.
    while tot > N and -pq[0] > tot // 2:
        curr = heapq.heappop(pq)
        curr *= -1
        #print(tot, curr)

        # If tot ever becomes 1, we return true because of an edge case with a length 2 array.
        # should only happen with an array of form [1, A] or [A, 1]
        # If tot becomes 0, we stop decreasing our array size.  Not a valid case as our tot > N && cannot
        # decrease further.  Happens in case of [9, 9, 9]
        # tot is now (SUM OF WHOLE ARRAY) - BIGGEST NUM IN ARRAY.
        # to complete the operation, to get prev biggest number we do, BIGGEST NUM IN ARRAY - (SUM OF WHOLE ARRAY) - BIGGEST NUM IN ARRAY
        tot -= curr
        if tot == 1: return True    # edge case 3
        if tot <= 0: return False   # edge case 2
        
        oldval = curr % tot
        tot += oldval
        heapq.heappush(pq, -oldval)
    
    return tot == N and all([num == -1 for num in pq])

if __name__ == "__main__":
    isPossible([1, 1, 1, 2])

