# Nathan Zhu April 28th, 2020.  Abouta take 376 final
# Leetcode 391 | hard | damn hard
# Category: Geometry
# 

def isRectangleCover(rectangles):
    """
    :type rectangles: List[List[int]]
    :rtype: bool
    """
    area = 0
    points = set()
    ca, getset = lambda x, y, X, Y: abs(X - x) * abs(Y - y), lambda x, y, X, Y: {(x, y), (x, Y), (X, y), (X, Y)}
    
    x1, y1, x2, y2 = float('inf'), float('inf'), float('-inf'), float('-inf')
    for x, y, X, Y in rectangles:
        x1 = min(x1, x)
        y1 = min(y1, y)
        x2 = max(x2, X)
        y2 = max(y2, Y)
        
        area += ca(x, y, X, Y)
        points ^= getset(x, y, X, Y)
        
    return ca(x1, y1, x2, y2) == area and getset(x1, y1, x2, y2) == points