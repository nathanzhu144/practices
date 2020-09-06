# /* Nathan Zhu Monday July 14th, 2020  Stockton, CA. Went to Nelson Park today.
# *  Deploying golang projects to Heroku is really fun.  :P
# *  Leetcode 1515 | hard | hard
# *  Category: Math, idea here is borrowed by gradient descent / hill climbing
# *
# *  Why would there one global minimal and no local minima?
# *  This is intuitively true.  So, the sum of convex functions is itself convex?
# *   https://leetcode.com/problems/best-position-for-a-service-centre/discuss/733215/Theory-and-Practice%3A-A-summary-of-methods
# */

import math
def getMinDistSum(positions):
    """
    :type positions: List[List[int]]
    :rtype: float
    """
    def get_dist(r, c):
        return sum([math.sqrt((r - posrow) ** 2 + (c - poscol) ** 2) for posrow, poscol in positions])
    
    # curr is chosen because positions is between 0 - 100
    # delta is chosen to be a value smaller than 10 ** -5
    curr, delta = 10.0, 0.000001
    r, c = 0, 0
    lastdist = get_dist(r, c)
    flag = False
    
    while curr >= delta:
        # flag is False when we haven't finished our search at this order of magnitude
        if flag: 
            curr /= 10
        # set flag to True, done w search at this order of mag if no move gives us a smaller dist
        flag = True
        
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newr, newc = curr * dr + r, curr * dc + c
            newdist = get_dist(newr, newc)
            # found closer square on order of mag
            if newdist < lastdist:
                flag = False
                r, c = newr, newc
                lastdist = newdist
                break     
    return lastdist

if __name__ == "__main__":
    print(getMinDistSum([[1,1],[3,3]]))