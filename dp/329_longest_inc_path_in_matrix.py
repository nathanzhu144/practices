# Nathan Zhu August 31st, 2019 10:45 pm
# Leetcode 329 | hard | hard
# Category: DP
# Google on-site.  Your interview score of 4.57/10 beats 76% of all users.
# Time Spent: 1 hour 59 minutes 25 seconds
# Time Allotted: 2 hours


# Input: nums = 
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:





class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def helper(row, col):
            key = (row, col)
            if key not in table:
                val = matrix[row][col]
                table[key] = 1 + max(helper(row + 1, col) if row < len(matrix) - 1 and val > matrix[row + 1][col] else 0,    
                                    helper(row, col + 1) if col < len(matrix[0]) - 1 and val > matrix[row][col + 1] else 0, 
                                    helper(row - 1, col) if row >= 1 and val > matrix[row - 1][col] else 0,             
                                    helper(row, col - 1) if col >= 1 and val > matrix[row][col - 1] else 0)
                
            return table[key]
        
        table = dict()
        ret = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ret = max(ret, helper(row, col))
                
        return ret