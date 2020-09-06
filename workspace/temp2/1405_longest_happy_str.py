
# /* Nathan Zhu Thursday July 23rd, 2020 7:30 am Stockton, CA.  Heroku is causing troubles again today.
# *  Leetcode 1405 | medium | medium (tho I kinda messed up, trickier than exp)
# *  Category: simulation
# */


def longestDiverseString(a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: str
    """
    # 1 2 3 
    # 2 1 3 
    # 2 3 1
    # 3 2 1
    def helper(a, b, c, ac, bc, cc):
        if a < b: return helper(b, a, c, bc, ac, cc)
        if b < c: return helper(a, c, b, ac, cc, bc)

        # at this point a >= b >= c
        # b == 0, c == 0
        if b == 0: return [min(a, 2) * ac]
        num_as = 2 if a > 1 else 1
        num_bs = 1 if a - num_as >= b else 0           # If we are to again choose a, the top letter, we must put a placeholder
                                                       # between a and next letter.  The way to check for this is a - num_as >= b
                                                       # Otherwise, we know there will be a role switch, so in that case we 
                                                       # just add as many as we can of the first & let the next recursive call
                                                       # choose which character to add next.

        return [num_as * ac] + [num_bs * bc] + helper(a - num_as, b - num_bs, c, ac, bc, cc)
    
    return "".join(helper(a, b, c, 'a', 'b', 'c'))


if __name__ == "__main__":
    print(longestDiverseString(4, 4, 3))