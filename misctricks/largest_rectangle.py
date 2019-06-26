# Nathan Zhu Monday June 24th, 10:02 am, Amex tower
# 
#  Idea is that we keep a max stack of heights, and a stack of their starting positions.
# If we ever find a height smaller than top of stack, we know that the rectangle must end there.
# We must still keep the position of the old rectangle starting position.
# Since the new rectangle is smaller than the top of the stack, we know that we can
# draw a rectangle starting from the position of the rectangle we popped off.  
#
# Keep popping until height stack is empty, or new rectangle is shorter than height at top of stack
    
# https://www.youtube.com/watch?v=VNbkzsnllsU
        #  Ok, so these two lines are really tricky...
        #
        #           4
        #         3 #
        #   2   2 # # 2
        #   # 1 # # # # 1 1 1 
        #   # # # # # # # # # 0
    # index 0 1 2 3 4 5 6 7 8 9
    # 
    # 
    # Pos Stack   Height Stack  
    #    -1
    #
    # Pos Stack   Height Stack  i == 0
    #     0            2
    #     -1
    # Pos Stack   Height Stack  i == 1 => rectangle ending at 0,  area == width * height == 
    #     1            1
    #     -1
    #
    # Pos Stack   Height Stack  i == 2   
    #     2            2
    #     1            1
    #     -1
    # 

import collections

def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    ''
    ## IMPORTANT ##
    # Appending a 0 to heights, ensures that height stack will be emptied in the end
    # pushing a -1 onto the stack ensures that stack will never be empty in any operation
    # ALSO, first index not in rectangle may be -1.  For example..
    
    heights.append(0)
    positions_stack = collections.deque([-1])   
    max_rectangle = 0
    
    for i in range(len(heights)):
        # we are continuing an old rectangle
        while heights[i] < heights[positions_stack[-1]]:
        
            height = heights[positions_stack.pop()]
            width = i - positions_stack[-1] - 1
            max_rectangle = max(max_rectangle, height * width)

        positions_stack.append(i)
    return max_rectangle

if __name__ == "__main__":
    print(largestRectangleArea([1, 1]))