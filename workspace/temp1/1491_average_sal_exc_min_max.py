# /* Nathan Zhu June 27th, 2020, Weekly contest crashed this week lol
# *  Leetcode 1491 | easy | easy
# *  Category: fizzbuzz
# */


def average(self, salary):
    """
    :type salary: List[int]
    :rtype: float
    """
    N = len(salary) - 2
    mins, maxs = min(salary), max(salary)
    proc = [n for n in salary if (n != mins and n != maxs)]
    return sum(proc) * 1.0 / N