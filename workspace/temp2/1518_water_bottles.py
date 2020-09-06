
# /* Nathan Zhu  Saturday July 11th, 2020 Stockton, CA, Weekly contest
# *  Leetcode 1518 | easy | easy
# *  Category: misc tricks
# */


def numWaterBottles(numB, numEx):
    """
    :type numBottles: int
    :type numExchange: int
    :rtype: int
    """
    ret = 0
    num_em = 0
    while numB > 0:
        ret += numB
        new_rem = (num_em + numB) % numEx
        numB = (num_em + numB) // numEx
        num_em = new_rem
    return ret