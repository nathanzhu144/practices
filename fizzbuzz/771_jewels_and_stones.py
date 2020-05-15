# Nathan Zhu May 7th, 2020 First day of work at Salesforce is coming up in a week-ish
# Leetcode 771 | easy | EZ
# Category: Fizzbuzz

def numJewelsInStones(self, J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    return sum([S.count(j) for j in J])