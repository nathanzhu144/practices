# /* Nathan Zhu  Saturday July 11th, 2020 Stockton, CA, Weekly contest
# *  Leetcode 1510 | hard | hard
# *  Category: minimax
# */


def winnerSquareGame(k):
    """
    :type n: int
    :rtype: bool
    """
    squares = []
    for i in range(1, k + 1):
        if i * i <= k: squares.append(i * i)
    table = dict()
    
    def helper(n):
        if n == 0: return False
        if n in table: return table[n]
        
        for sq in squares:
            neigh = n - sq
            if neigh < 0: break
            if not helper(neigh): 
                table[n] = True
                return table[n]
        
        table[n] = False
        return False
    
    return helper(k)
        