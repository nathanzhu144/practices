# Nathan Zhu Thurs Jan 29th, 2020 North Campus, Courtyards, 7:00 pm, about to go to Coco's 
# Leetcode 1035 | medium | LOL
# Category: I never realized this was just finding the LCS of the two integers man.  Broooo


def maxUncrossedLines(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    R, C = len(A), len(B)
    
    table = [[0 for c in range(C + 1)] for r in range(R + 1)]
    
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if A[r - 1] == B[c - 1]: table[r][c] = table[r - 1][c - 1] + 1
            elif table[r - 1][c] > table[r][c - 1]: 
                table[r][c] = table[r - 1][c]
            else:
                table[r][c] = table[r][c - 1]
                
    return table[-1][-1]