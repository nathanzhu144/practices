# Nathan Zhu Christmas Day, Dec 25th, 2019, but written on paper on way back from ski trip Dec 23rd, 2019
# Leetcode 991 | medium | medium
# Category: Misc tricks, greedy, naive soln with BFS
# 
# Don't do a BFS on this one, lol.  It works only for small numbers and needs mathematical insight to
# do the actual soln.
# Runtime is (X - Y) if this is positive + log(Y - X) if this is positive.
# Not too sure about runtime.

# On a broken calculator that has a number showing on its display, we can perform two operations:
#
# Double: Multiply the number on the display by 2, or;
# Decrement: Subtract 1 from the number on the display.
# Initially, the calculator is displaying the number X.
#
# Return the minimum number of operations needed to display the number Y.
def brokenCalc(X, Y):
    """
    :type X: int
    :type Y: int
    :rtype: int
    """
    # Going from Y -> X, backwards, we have two operations we can do,
    # we can divide by 2
    # we can add 1
    #
    # can kind of guess more about which way to go, as if Y is odd, we can only add 1
    #
    #
    # If Y is smaller than X, dividing by 2 will only make a longer path, so we only add
    # 1 until we get to X. 
    # 
    # If Y is bigger than X, we have to divide at some point, but as Y can be odd at some
    # points, we may have to add 1 before divididing again.  
    #
    # IMPORTANT: WE NEVER ADD 1 twice when Y is bigger than X.
    #
    # Proof: 
    #         Suppose (Y + 1) / 2 == Z                    [Y + 1 is even, Z is integer]
    #                 (Y + 1 + 1) / 2                     [Invalid, Y + 2 is odd]
    #                 (Y + 1 + 1 + 1) / 2 = Z + 1         
    #                 (Y + 1 + 1 + 1 + 1) / 2             [Invalud, Y + 4 is odd]
    #                 (Y + 1 + 1 + 1 + 1 + 1) / 2 = Z + 2 
    #                 
    # Note that a shorter way to get to Z + 1 and Z + 2 is simply doing (Y + 1) / 2 + 1 
    #                                                                or (Y + 1) / 2 + 1 + 1
    # 
    def helper(Y, X):
        ret = 0
        while Y > X:
            if Y & 1: Y += 1   # If Y is odd, add 1
            else: Y /= 2       # If Y is even, divide by 2
            ret += 1

        return ret + X - Y     # X >= Y at this point, so we add 1 until we get to X
    
    return helper(Y, X)