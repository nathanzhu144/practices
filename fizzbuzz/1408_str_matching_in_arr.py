# Nathan Zhu April 11th, 2020. Stockton, CA.  COVID-19
# Leetcode 1408 | easy | easy for brute force
# Category: Suffix tree?
# 
def stringMatching(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    ret = []
    N = len(words)
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if words[i] in words[j]: 
                ret.append(words[i])
                break
                
    return ret