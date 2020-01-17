# Nathan Zhu Jan 13th, 2020 Volkovitch 376 lecture, he's proving Euclid's algo is LogN
# Leetcode 311 | medium | hard
# Category: Misc tricks
# I think the trick here is somewhat unintuitive, and I don't completely
# understand it yet, but I think I can work out the trick in an interview now.


def multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if not A or not B: return None
    m, n, newcols = len(A), len(A[0]), len(B[0])
    
    ret = [[0 for _ in range(newcols)] for _ in range(m)]
    b_dict = {}
    
    for k, row in enumerate(B):
        b_dict[k] = {}
        for j, num in enumerate(row):
            if num: b_dict[k][j] = num
                
    for i, row in enumerate(A):
        for k, eleA in enumerate(row):
            if eleA:
                for j, eleB in b_dict[k].iteritems():
                    ret[i][j] += eleA * eleB
    return ret