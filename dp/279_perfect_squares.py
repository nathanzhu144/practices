
# Nathan Zhu August 27th, 2019, 2:09 pm 
# Leetcode 279 | medium | EZ yo
# Category: BFS or DP
#

# Done in real-time in a "Google on-site interview", 1 hour 59 min spent for 2 hour interview
# Not sure what rating was

Time Allotted: 2 hours

Google on-site


Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        # Two approaches:
        # 1. BFS (done before)
        # 2. DP  (let me try this)
        #
        #  DP Idea .
        #  We can re-store the least num of perfect squares for numbers 
        #  smaller than current number.  If we ever get to that number,
        #  we don't need to recalculate.
        #
        # 
        #  Data Structures
        #  table  (hash table)  from int (number) -> int (least number of perf sq)
        # 
        #  Algorithm
        #  Number like X
        # 
        #  1, 4, ... int(sqrt(X))
        #  We try subtracting all of these, keep track of the minimum
        #  number of numbers that we need.
        #
        #  If we get to a base case of 0, we return.
        
        
        
        # Returns an int
        def helper(num, table):
            if num in table: return table[num]

            # base cases
            if num == 0: return 0
            if num < 0: return float('inf')

            least = float('inf')
            for i in range(1, int(num ** 0.5) + 1):
                least = min(least, 1 + helper(num - i * i, table))

            table[num] = least
            return table[num]

        return helper(n, dict())