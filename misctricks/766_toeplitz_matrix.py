# Nathan Zhu August 29th, 2019 12:58 am
# Leetcode 766 | easy | EZ
# Google- On-Site Interview
# Completed August 29, 2019 12:58 AM
# Your interview score of 6.04/10 beats 87% of all users.
# Time Spent: 1 hour 30 minutes 12 seconds
# Time Allotted: 2 hours


# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 
# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]
# Output: True

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row in range(len(matrix) - 1):
            for col in range(len(matrix[0]) - 1):
                if matrix[row][col] != matrix[row + 1][col + 1]: return False
                
        return True