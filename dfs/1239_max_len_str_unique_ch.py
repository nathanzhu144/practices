# Nathan Zhu April 15th, 2020.  11:38 pm.  Stockton, CA.  JSW lost his pos at extrahop today.  :(
# Leetcode 1239 | medium | easy
# Category: DFS

def maxLength(arr):
    """
    :type arr: List[str]
    :rtype: int
    """
    ret = [0]
    
    def dfs(idx, curr):
        if idx >= len(arr): return
        for i in range(idx, len(arr)):
            newword = arr[i] + curr
            if len(set(newword)) == len(newword):
                ret[0] = max(ret[0], len(newword))
                dfs(i + 1, newword)
                
    dfs(0, "")
    return ret[0]
                    