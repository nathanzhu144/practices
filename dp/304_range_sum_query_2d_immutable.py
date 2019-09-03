# Nathan Zhu Monday August 12th, 2019.  7:38 pm, Feels kinda strange to not be at work today. New York seems so far away, but so close.
# Leetcode 304 | medium | medium if you see the picture and understand pre-sum
# Here's the idea for range sum query two.
# +-----+-+-------+     +--------+-----+     +-----+---------+     +-----+--------+
# |     | |       |     |        |     |     |     |         |     |     |        |
# |     | |       |     |        |     |     |     |         |     |     |        |
# +-----+-+       |     +--------+     |     |     |         |     +-----+        |
# |     | |       |  =  |              |  +  |     |         |  -  |              |
# +-----+-+       |     |              |     +-----+         |     |              |
# |               |     |              |     |               |     |              |
# |               |     |              |     |               |     |              |
# +---------------+     +--------------+     +---------------+     +--------------+

#    sums[i][j]      =    sums[i-1][j]    +     sums[i][j-1]    -   sums[i-1][j-1]   +  

#                         matrix[i-1][j-1]
# So, we use the same idea to find the specific area's sum.

# +---------------+   +--------------+   +---------------+   +--------------+   +--------------+
# |               |   |         |    |   |   |           |   |         |    |   |   |          |
# |   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |          |
# |   +------+    |   |         |    |   |   |           |   +---------+    |   +---+          |
# |   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)    |
# |   |      |    |   |         |    |   |   |           |   |              |   |              |
# |   +------+    |   +---------+    |   +---+           |   |              |   |              |
# |        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |              |
# +---------------+   +--------------+   +---------------+   +--------------+   +--------------+


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        
        # Data Structures
        # self.presum[row][col] is the NOT sum of all matrix elements from matrix[0][0] up to including matrix[row][col].
        #                       it is the area of the rectangle starting at sq (0, 0), and ending at (row, col) inclusive/
        self.presum = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 and col == 0: self.presum[row][col] = matrix[row][col]
                elif row == 0 and col != 0: self.presum[row][col] = self.presum[row][col - 1] + matrix[row][col]
                elif col == 0 and row != 0: self.presum[row][col] = self.presum[row - 1][col] + matrix[row][col]
                # We add an area twice, so we subtract one of that area.
                else: self.presum[row][col] = self.presum[row - 1][col] + self.presum[row][col - 1] + matrix[row][col] - self.presum[row - 1][col - 1]
                

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = self.presum[row2][col2]
        if row1 - 1 >= 0: ret -= self.presum[row1 - 1][col2]
        if col1 - 1 >= 0: ret -= self.presum[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0: ret += self.presum[row1 - 1][col1 - 1]
        
        return ret



if __name__ == "__main__":
    c1 = NumMatrix([[3]])
    c1.sumRegion(0, 0, 0, 0)


    1
    -7