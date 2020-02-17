# Nathan Zhu Feb 10th, 2020. During 481 lecture
# Leetcode 575 | easy | EZ
# Category: misc tricks
# This question is kinda dumb tbh.  Figures microsoft would ask this question

def distributeCandies(candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    return min(len(candies) // 2, len(set(candies)))