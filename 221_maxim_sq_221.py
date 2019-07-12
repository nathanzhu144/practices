# Nathan Zhu, YOTEL New York 10:35 am July 6th. 2019

def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    mem = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
    max_sq = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if not row or not col: 
                mem[row][col] = int(matrix[row][col])
                max_sq = max(max_sq, mem[row][col])
            if row and col and matrix[row][col] == "1":
                mem[row][col] = min(int(mem[row - 1][col]), int(mem[row][col - 1]), int(mem[row - 1][col - 1])) + 1
                max_sq = max(max_sq, mem[row][col])

    return max_sq ** 2

if __name__ == "__main__":
    print(maximalSquare([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]))