# Nathan Zhu Stockton, CA. Sunday May 31st, 2020 9:10 pm PST.
# Leetcode 165 | medium | easy
# Category: fizzbuzz

def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1, v2 = version1.split("."), version2.split(".")
    for i in range(max(len(v1), len(v2))):
        val1 = int(v1[i]) if i < len(v1) else 0
        val2 = int(v2[i]) if i < len(v2) else 0
        if val1 < val2: return -1
        if val1 > val2: return 1
            
    return 0