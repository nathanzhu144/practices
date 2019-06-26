    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        curr_row = [0, 1, 0]
        returned = list()
        
        for j in range(numRows):
            returned.append(curr_row[1:-1])  
            next_row = list()
            for i in range(len(curr_row) - 1):
                next_row.append(curr_row[i] + curr_row[i + 1])
            curr_row = [0] + next_row + [0]   
            
        return returned