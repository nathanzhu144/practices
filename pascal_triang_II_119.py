    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        curr_row = [0, 1, 0]
        for row in range(rowIndex):
            next_row = list()
            for i in range(len(curr_row) - 1):
                next_row.append(curr_row[i] + curr_row[i + 1])
            curr_row = [0] + next_row + [0]
                
            
        
        return curr_row[1:-1]