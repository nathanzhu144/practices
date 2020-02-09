# Nathan Zhu Jan 20th, 2020 9:45 pm, Just called George about serialize-deserialize binary tree /
#                                    critical connections.  Good time.
# Leetcode 406 | medium | not too bad given insight.
# Runtime N^2
# Category: Sorting

def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    
    # Insight, the highest person - height 7, only cares about the positions of the 
    # people with height equal to 7.
    #
    # The next highest person, 6, only cares about their relative position in the line compared
    # to the other 6s, and 7s.
    #
    # ...
    #
    # [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    # Sort by two things: 
    # 1. Sort by decreasing height
    # 2. Sort by increasing position
    people.sort(key = lambda x: (-x[0], x[1]))
    
    ret = []
    for height, pos in people:
        ret.insert(pos, [height, pos])
    
    return ret
    