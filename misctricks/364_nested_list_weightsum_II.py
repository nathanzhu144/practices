# Nathan Zhu EHS 55 John Street, Last week of internship, 10th week of doing Leetcode, Tuesday August 6th, 2019
# Leetcode 364 | medium | medium
# Category: Misc
# 
# Question:
# Input: [1,[4,[6]]]
# Output: 17 
# Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
#         
# 
# For future readers, this is a key fact I used when understanding this algorithm:
# Each integer get added one extra time for the mere existence of each one level under it.
# 
# The concept of weight here is implemented with repeated addition;
#
# This is a pretty intuitive algorithm.  
# Uses a similar algorithm as leetcode 339, nested list weight sum I.




def depthSumInverse(nestedList):
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """
    weighted, unweighted = 0, 0
    currlv = nestedList[:]
    
    while currlv:
        nextlv = []
        
        for item in currlv:
            if item.isInteger(): unweighted += item.getInteger()
            else: nextlv.extend(item.getList())
                
        currlv = nextlv
        weighted += unweighted
    
    return weighted