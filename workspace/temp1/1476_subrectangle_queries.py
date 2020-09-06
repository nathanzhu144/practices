# /* Nathan Zhu June 13th, 2020  
# *  Leetcode 1476 | medium | not sure how to optimize thi
# *  Category: Design
# */



class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.arr = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """;
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.arr[r][c] = newValue
        

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        
        return self.arr[row][col]