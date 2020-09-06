
# /* Nathan Zhu Friday July 24rd, 2020 5:34 am Stockton, CA.  Rak joined leetcode group yesterday.  Also, watching kissing booth 2 apparently.
# *  Leetcode 1316 | hard | getting from N^3 -> N^2 seems pretty hard
# *  Category: misc trick
# */


def distinctEchoSubstrings(text):
    """
    :type text: str
    :rtype: int
    """
    # Simple N ^ 3 solution
    # Intuition: Brute force, split on every possible division point while
    #            increasing sizes to left and right.
    #
    
    N = len(text)
    ret = 0
    visited = set()
    for i in range(N):
        for sz in range(1, N):
            if (i - sz + 1 < 0) or (i + sz + 1 > N): break
            left = text[i - sz + 1 : i + 1]
            right = text[i + 1: i + 1 + sz]
            
            if left not in visited and left == right:
                #print(text[i - sz + 1 : i + 1])
                visited.add(left)
                ret += 1
                
    return ret