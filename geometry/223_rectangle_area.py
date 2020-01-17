
# Nathan Zhu 6:57 pm January 2nd, 2019 Just for back from santa cruz yesterday at point lobos.
# Leetcode 223 | medium | hard
# Category: Geometry.

# Dude I sux at geomertry
# See Leetcode 836 approach 2 for intuition.

import collections

def computeArea(self, A, B, C, D, E, F, G, H):
    """
    :type A: int
    :type B: int
    :type C: int
    :type D: int
    :type E: int
    :type F: int
    :type G: int
    :type H: int
    :rtype: int
    """
    Rectangle = collections.namedtuple('Rectangle', ['leftx', 'lefty', 'rightx', 'righty'])
    r1, r2 = Rectangle(A, B, C, D), Rectangle(E, F, G, H)
    
    r1_area = abs(r1.leftx - r1.rightx) * abs(r1.lefty - r1.righty)
    r2_area = abs(r2.leftx - r2.rightx) * abs(r2.lefty - r2.righty)
    
    bottom_len = min(r1.rightx, r2.rightx) - max(r1.leftx, r2.leftx)
    side_len = min(r1.righty, r2.righty) - max(r1.lefty, r2.lefty)
    
    if bottom_len <= 0 or side_len <= 0: return r1_area + r2_area
    else: return r1_area + r2_area - (side_len * bottom_len)