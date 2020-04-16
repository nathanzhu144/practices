# Nathan Zhu Sunday, April 13th, 2020. 10:35 pm.  Stockton, CA, Covid-19 lockdown
# Leetcode 1229 | medium | EZ
# Categoy: Intervals

def minAvailableDuration(slots1, slots2, duration):
    """
    :type slots1: List[List[int]]
    :type slots2: List[List[int]]
    :type duration: int
    :rtype: List[int]
    """
    slots1.sort()
    slots2.sort()
    i1, i2 = 0, 0
    
    while i1 < len(slots1) and i2 < len(slots2):
        s1, s2 = slots1[i1], slots2[i2]
        intersect = [max(s1[0], s2[0]), min(s1[1], s2[1])]
        if intersect[1] - intersect[0] >= duration: return [intersect[0], intersect[0] + duration]
        
        # Whichever free slot has a larger ending time, we want to keep
        if s1[1] > s2[1]: i2 += 1
        else: i1 += 1
            
    return []