# /* Nathan Zhu Monday July 14th, 2020  Stockton, CA. Went to Nelson Park today.
# *  Deploying golang projects to Heroku is really fun.  :P
# *  Leetcode 1505 | hard | hard
# *  Category: binary search
# */



from collections import defaultdict, deque
from sortedcontainers import SortedList
from string import digits
import string
import bisect

# Suppose we are looking at "722" 
#  number 7 2 2
#  idx   0 1 2


# After first swap
#  number 2 7 2 <- this two is overestimated
#   idx   0 1 2

# idx_dict = [2] -> [2]
#            [7] -> [1]
# used = [2]

# Note that next 2 is overestimated by 1; it takes only one swap to move it to correct
# position.  To figure out the new position of the two, or any digit we are trying to move up,
# we look at all the numbers "used" already.  We take all the numbers to the "left" of the 
# current digit under consideration.  All digits moved from the left, decrease the number of swaps by 1.
# We can do this with a SortedList easily, as we can do a binary search to count number of numbers to left.
# This should be a bisect_right as any same numbers used should be counted to the left. 

def minInteger(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    index_dict = defaultdict(deque)
    used = SortedList()
    ret = []
    N = len(num)
    
    for i, num in enumerate(num):
        index_dict[num].append(i)
        
    for i in range(N):
        for digit in digits:
            if not index_dict[digit]: continue
            idx = index_dict[digit][0]
            num_swaps = idx - used.bisect_right(idx)
            
            if num_swaps <= k:
                k -= num_swaps
                ret.append(digit)
                used.add(idx)
                index_dict[digit].popleft()
                break

    return "".join(ret)

if __name__ == "__main__":
    print(minInteger("435282",7))