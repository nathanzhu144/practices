# Nathan Zhu January 3rd, 2019 12:39 am Kinda tired, but I have finished more than 26 leetcode problems today
# Leetcode 59 | medium | medium
# Category: Fizzbuzz / misc tricks

# Problem:
# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

def generateMatrix(self, n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    ret = [[0 for col in range(n)] for row in range(n)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cnt, idx = 0, 1
    bounds = [n, n - 1]
    r, c = 0, -1
    
    while bounds[cnt % 2] > 0:
        for i in range(bounds[cnt % 2]):
            r += directions[cnt % 4][0]
            c += directions[cnt % 4][1]
            ret[r][c] = idx
            idx += 1
        bounds[cnt % 2] -= 1
        cnt += 1
        
    return ret