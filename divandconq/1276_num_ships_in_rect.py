# Nathan Zhu
# Leetcode 1276 | hard | fun question
# Category: Divide and conq
# Went climbing today, they took out a cool purple v1 overhang that I really liked.
# 
# Thinking:
# This is an O(N) algorithm, where N is the number of points in the grid.
# T(n) = 4xT(n/4) + O(1)
# There are at most 
#    A
#   /\ \  \
#   1 2 3 4
#  /\   /\
# 1  2 3  4
# 
# Realistically, we only have 10 nodes per level.


def countShips(sea, topRight, bottomLeft):
    """
    :type sea: Sea
    :type topRight: Point
    :type bottomLeft: Point
    :rtype: integer
    """
    def helper(tr, bl):
        if tr.x == bl.x and tr.y == bl.y and sea.hasShips(tr, bl):
            return 1
        if tr.x < bl.x or tr.y < bl.y:
            return 0
        if not sea.hasShips(tr, bl):
            return 0
        mid_x = (tr.x + bl.x) // 2
        mid_y = (tr.y + bl.y) // 2
        return helper(Point(mid_x, tr.y), Point(bl.x, mid_y + 1)) + helper(tr, Point(mid_x + 1, mid_y + 1)) + \
                + helper(Point(mid_x, mid_y), bl) + helper(Point(tr.x, mid_y), Point(mid_x + 1, bl.y))
    
    return helper(topRight, bottomLeft)