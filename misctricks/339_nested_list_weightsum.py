# Nathan Zhu EHS 55 John Street.  Tuesday August 6th, 2019. 10th week of doing leetcode. Last week of internship.  Final presentations today.
# Leetcode 339 | easy | easy
# Category: Misc tricks
# Figuring out the lib functions for nestedlist was most confusing part.
#                     
# 


# So we go through a nested list object.
# Add all integers in current depth to ret
# Send brackets to next depth.

# level = 1
# curr = [1,[4,[6]], [1]]
# ret = 0

# level = 2
# curr = [4, [6], 1]
# ret = 1

# level = 3
# curr = [6]
# ret = 11

# level = 4
# ret = 29


def depthSum(nestedList):
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """
    currlv = nestedList[:]
    ret = 0
    level = 1

    while currlv:
        nextlv = []
        for curri in currlv:
            if curri.isInteger(): ret += (curri.getInteger() * level)
            else: nextlv.extend(curri.getList())
        currlv = nextlv
        level += 1
    return ret