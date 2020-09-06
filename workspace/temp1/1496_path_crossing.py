# /* Nathan Zhu June 27th, 2020, Weekly contest crashed this week lol
# *  Leetcode 1496 | easy | easy
# *  Category: mis tricks
# */
# Similar to cycle in linked list


def isPathCrossing(self, path):
    """
    :type path: str
    :rtype: bool
    """
    table = dict()
    table['N'] = (-1, 0)
    table['E'] = (0, 1)
    table['S'] = (1, 0)
    table['W'] = (0, -1)
    
    visited = set()
    visited.add((0, 0))
    curr = (0, 0)
    
    for ch in path:
        newr, newc = curr[0] + table[ch][0], curr[1] + table[ch][1]
        newpos = (newr, newc)
        if newpos in visited: return True
        visited.add(newpos)
        curr = newpos
        
    return False