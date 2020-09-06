# /* Nathan Zhu Snowflake OA, for Fall Co-op June 11th, 2020
# *  Leetcode n/a | n/a | medium
# *  Category: monotonic stack
# There was a fancy description for a simple thing.
# You are given an array of numbers.  You want to find the maximum minimum or minimum maximum
# where the minimum/maximum is over k consecutive elements.

import collections
def segment(x, space):
    # Write your code here
    ret = float('-inf')
    q = collections.deque()
    for i, num in enumerate(space):
        while q and q[0][1] <= i - x: q.popleft()
        while q and q[-1][0] >= num: q.pop()
        q.append([num, i])
        if q and i >= x - 1: ret = max(q[0][0], ret)
    
    return ret



if __name__ == "__main__":
    print(segment(1, [0, 2, 3]))