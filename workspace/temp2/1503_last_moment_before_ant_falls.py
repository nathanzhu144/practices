# /* Nathan Zhu Monday July 14th, 2020  Stockton, CA. Went to Nelson Park today.
# *  Deploying golang projects to Heroku is really fun.  :P
# *  Leetcode 1503 | medium | lol dang didn't get this
# *  Category: misc tricks
# When two ants bump into each other, since we don't care which ant is which, we can treat as "going thru"
# each other.  

def getLastMoment(n, left, right):
    """
    :type n: int
    :type left: List[int]
    :type right: List[int]
    :rtype: int
    """

    return max(n - min(right) if right else 0, max(left) if left else 0)