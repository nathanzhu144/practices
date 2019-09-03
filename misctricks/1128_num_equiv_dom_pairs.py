# Nathan Zhu August 31, 2019 2:24 pm
# Random Set- Online Assessment
# Your interview score of 4.60/10 beats 48% of all users.

# Questions 
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if
# and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated 
# to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] 
# is equivalent to dominoes[j].

# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1


from math import factorial

def numEquivDominoPairs(self, dominoes):
    """
    :type dominoes: List[List[int]]
    :rtype: int
    """
    def ncr(n, r):
        return factorial(n) // factorial(r) // factorial(n - r)
    
    table = collections.defaultdict(int)
    ret = 0
    for domino in map(tuple, dominoes):
        if domino and domino[::-1] not in table:
            table[domino] += 1
            
        else:
            if domino in table: table[domino] += 1
            else: table[domino[::-1]] += 1
    
    for keys, val in table.items():
        if val >= 2: ret += ncr(val, 2)
        
    return ret