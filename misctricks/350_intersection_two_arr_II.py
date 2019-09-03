# Nathan Zhu Thursday August 22nd, 2019 2:38 pm.  Stockton California
# Leetcode 350 | easy | EZ
# Category: Misc, Using a set lol



def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
    ret = list()
    
    for num in c1: 
        if num in c2:
            ret.extend([num] * min(c1[num], c2[num]))
            
    return ret