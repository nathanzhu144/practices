# Nathan Zhu August 29th, 2019 12:58 am
# Leetcode 299 | easy | EZ
# Category: Hash table
# 
# Google on-site interview
# Your interview score of 6.04/10 beats 87% of all users.
# Time Spent: 1 hour 30 minutes 12 seconds
# Time Allotted: 2 hours

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        digits = collections.Counter(secret)
        cows, bulls = 0, 0
        for num in guess: 
            if digits[num] > 0: 
                cows += 1
                digits[num] -= 1
                
        for i in range(len(secret)): 
            if secret[i] == guess[i]: bulls += 1
                
        return "".join([str(bulls), "A", str(cows - bulls), "B"])