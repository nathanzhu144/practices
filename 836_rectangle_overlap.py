
import collections

# Intuition
# Two rectangles DO NOT overlap if one of these 2 conditions are true.
# 1. one rectangle is on top of another rectangle
# 2. one rectangle is to the left of another rectangle
#
# The above 4 are sufficient to chese the 2 conditions, and since 
# we want to see if they overlap, we return the negation of this value.
def isRectangleOverlap(rec1, rec2):
    """
    :type rec1: List[int]
    :type rec2: List[int]
    :rtype: bool
    """
    Rectangle = collections.namedtuple('Rectangle', ['leftx', 'lefty', 'rightx', 'righty'])
    r1, r2 = Rectangle(*rec1), Rectangle(*rec2)
    
    return not(r1.leftx >= r2.rightx or r1.lefty >= r2.righty or r1.rightx <= r2.leftx or r1.righty <= r2.lefty)




# Intuition behind this one:
# 
# How to calculate area of intersection of two rectangles?
# 
# Think in 1D for a second.  We take two vertical lines:
#   T1 (5)
#   |
#   |          T2 (3)
#   |          |
#   |          |
#   B1 (1)     | B2(0)
# 
# How do we find overlap of these two intervals? 
# min(T1, T2) - max(B1, B2)
#
# if these DONT overlap, min(T1, T2) <= max(B1, B2), and this above expr is negative.
# 
# Again, take two horizontal lines.  We can do the same thing.  If we just care whether two
# rectangles overlap (as here) we can just return true if both of these are above 0.
# However, we can also derive the area from these too quite easily.
# 
#
def isRectangleOverlap2(rec1, rec2):
    """
    :type rec1: List[int]
    :type rec2: List[int]
    :rtype: bool
    """
    Rectangle = collections.namedtuple('Rectangle', ['leftx', 'lefty', 'rightx', 'righty'])
    r1, r2 = Rectangle(*rec1), Rectangle(*rec2)
    
    
    n_left_x = max(r1.leftx, r2.leftx)
    n_right_x = min(r1.rightx, r2.rightx)
    
    n_left_y = max(r1.lefty, r2.lefty)
    n_right_y = min(r1.righty, r2.righty)
    
    return n_left_x < n_right_x and n_left_y < n_right_y

if __name__ == "__main__":
    print(isRectangleOverlap2([-10,-4,-3,2],[-3,-4,5,3]))