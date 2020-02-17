# Nathan Zhu Feb 14th, 2020. 10:00 pm Foundry Lofts We went to Aventura's today for Valentine's.  Was a good time.
# Leetcode 22 | medium | easy
# Category: Backtracking

# I get better at coding this everytime.
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    ret = []
    # cnt represents number open
    def helper(n, curr, cnt):
        if n < 0 or cnt < 0: return
        if n == 0 and cnt == 0: ret.append(curr)

        helper(n - 1, curr + "(", cnt + 1)
        helper(n, curr + ")", cnt - 1)
            
    helper(n, "", 0)
    
    return ret
        