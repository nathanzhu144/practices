
# /* Nathan Zhu Monday July 4th, 2020  Stockton, CA. 
#    Leetcode 1504 | medium | medium
#    Category: Misc tricks
# */


def numSubmat(mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    R, C = len(mat), len(mat[0])
    
    def count(sr, sc):
        ret = 0
        r, c, minc = sr, sc, -1
        while r >= 0:
            curr = 0
            while c >= 0:
                if mat[r][c] == 0 or c == minc: 
                    minc = max(c, minc)
                    break
                curr += 1
                c -= 1
            ret += curr
            c = sc
            r -= 1
            
        return ret
    
            
    ret = 0
    for r in range(R):
        for c in range(C):
            ret += count(r, c)
    return ret