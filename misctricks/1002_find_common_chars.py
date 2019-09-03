# Nathan Zhu Thursday August 22nd, 2019 3:16 pm Stockton California
# Leetcode 1002 | easy | EZ
# Category: Misc
#
# Given an array A of strings made only from lowercase letters, return a list of all characters 
# that show up in all strings within the list (including duplicates).  
# 
# This is the same as list intersection II, but with a bunch of lists.
#

def commonChars(A):
    """
    :type A: List[str]
    :rtype: List[str]
    """
    def find_intersection(s1, s2):
        ret = list()
        c1, c2 = collections.Counter(s1), collections.Counter(s2)
        for character in c1: ret.extend([character] * min(c1[character], c2[character]))
        return "".join(ret)
    
    arr = collections.deque(A)
    while len(arr) > 1:
        arr.append(find_intersection(arr[0], arr[1]))
        arr.popleft()
        arr.popleft()
        
    return arr[0]