# Nathan Zhu January 2nd, 2019 2:30 pm
# Leetcode 593 | medium | hard
# The idea in this is in the notes file at the bottom, but the general idea is that,
# given a center of square and a vertex, it is very easy to calculate the other 3 vertices with simple
# linear algebra.  
#
# We vertify the 3 points we calculate against the actual points, and if all are the same, it must be a square.

def validSquare(p1, p2, p3, p4):
    """
    :type p1: List[int]
    :type p2: List[int]
    :type p3: List[int]
    :type p4: List[int]
    :rtype: bool
    """
    if p1 == p2 == p3 == p4: return False  # if all points are same, not considered square

    # reason for custom find function is to search a list for a point, and equating things like (1.0, 1.0) and (1, 1)
    epsilon = 0.0001
    def find(x):
        for pt in rest:
            if abs(x[0] - pt[0]) < epsilon and abs(x[1] - pt[1]) < epsilon: return True
        return False
    
    # calculating center coord
    center_x = (p1[0] + p2[0] + p3[0] + p4[0]) / 4.0   # 4.0 is IMPORTANT. WILL FLOOR IN PYTHON2 OTHERWISE.
    center_y = (p1[1] + p2[1] + p3[1] + p4[1]) / 4.0
    center = (center_x, center_y)
    
    # calculating two perpendicular vectors from center to vertices of square.
    # We use p1 to calculate the vertices, and verify that against v2, v3, v4
    v1 = [p1[0] - center[0], p1[1] - center[1]]
    v2 = [-v1[1], v1[0]]

    rest = set(map(tuple, [p2, p3, p4]))
    B = (center[0] - v1[0], center[1] - v1[1])
    C = (center[0] - v2[0], center[1] - v2[1])
    D = (center[0] + v2[0], center[1] + v2[1])

    return find(B) and find(C) and find(D)


if __name__ == "__main__":
    print(validSquare([0,0],[1,1],[1,0],[0,1]))
    print(validSquare([0,0],[-1,0],[1,0],[0,1]))