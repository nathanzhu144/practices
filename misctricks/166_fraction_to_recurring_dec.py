# Nathan Zhu Monday Nov 25th, 2019 2:12 pm.
# Leetcode 166 | medium | pretty hard if you don't see the insight.
# Category: misctricks

# The insight here is actually largely mathematical.  A recurring decimal occurs when we are faced
# with the same numerator and denominator.  However, since the denominator never changes, if we get the
# same numerator again, we know that we have a recurring decimal.
#
# Another cool thing here is finding if two numbers have opposite signs.
# (numerator ^ denominator) < 0
# Idea is sign bit in an XOR is flipped iff one of the two is negative.
# 
# Edge cases:
# -0
# Dividing with negative numerator can cause problems...
# 

def fractionToDecimal(numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    if denominator == 0: return None                 # dividing by 0 is not allowed.
    if numerator == 0: return "0"                    # prevents -0
    front = ""
    
    # Finding the sign, if we XOR two numbers with opposite sign, sign bit is negative still
    if (numerator ^ denominator) < 0: front += "-"
    
    # The algorithm gets messed up with negative numbers.
    numerator, denominator = abs(numerator), abs(denominator)
    
    front += str(numerator // denominator)
    numerator = numerator % denominator
    
    if numerator == 0: return front
    
    # this is finding the decimal part
    front += "."
    visited = dict()
    back, index = [], 0
    while numerator != 0:
        # Keep track of when we saw this numerator for if we see it again.
        visited[numerator] = index
        
        numerator *= 10
        back += str(numerator // denominator)
        numerator = numerator % denominator
        
        # We see a repeated numerator, indicating we have a repeat here.
        if numerator in visited:
            idx = visited[numerator]
            back.insert(idx, "(")
            
            return front + "".join(back) + ")"
        index += 1
        
    # No repeat.
    return front + "".join(back)