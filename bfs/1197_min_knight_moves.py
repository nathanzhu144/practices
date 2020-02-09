# Nathan Zhu Tuesday Jan 21st, 2020 Ugli 4th floor near the birds roost.  I do not hear the birds?  Where are the crows?
# Leetcode 1197 | medium | medium?
# Category: BFS
#
# There's a math way to do this in O(1) time but I didn't think too hard about it.  The BFS way is more
# generalizable, and I actually wrote a bidirectional BFS.
#
# One trick to shrink search space is you can convert (-4, 3) -> (4, 3) as by symmetry
# the number of ways to get there are the same.  Also, (3, 4) has same steps as (4, 3), so you can
# further reduce search space by on searching for points where (a, b) and a <= b.


def minKnightMoves(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    if (x > y): return self.minKnightMoves(y, x)
    
    x, y = abs(x), abs(y)
    if (x, y) == (0, 0): return 0
    offsets = [
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (2, 1), (2, -1), (-2, 1), (-2, -1)
    ]
    # BFS1 starts at (0, 0) and BFS2 starts at (x, y)
    # Level is a set that represents current nodes for BFS1 and BFS2
    # Visited is visited set for each BFS, respectively.
    # The while loop alternates doing a step for BFS1 and BFS2
    level, visited, step = [{(0, 0)}, {(x, y)}], [set(), set()], 0
    i = 0
    while True:
        i = (i + 1) & 1
        visited[i] |= level[i]
        temp = set()
        for xx, yy in level[i]:
            for dx, dy in offsets:
                newx, newy = xx + dx, yy + dy
                coord = (min(newx, newy), max(newx, newy))
                # Checks if BFS1 found BFS2 or BFS2 found BFS1
                if coord in visited[1 - i]:
                    return step
                if coord not in visited[i] and -2 <= newx and -2 <= newy:
                    temp.add(coord)

        level[i], step = temp, step + 1

if __name__ == "__main__":
    print(minKnightMoves(217, 47))