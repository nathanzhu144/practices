# Nathan Zhu August 30th, 2019 1:17 am
# Leetcode 205 | easy | EZ
# Category: string / hashtable
# Done in mock google on-site interview
# Your interview score of 6.36/10 beats 87% of all users.
# Time Spent: 1 hour 23 minutes 49 seconds
# Time Allotted: 2 hours

# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order
#  of characters. No two characters may map to the same character but a character may map to itself.



class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # The idea here is that we want to figure out whether the 
        # Let's define a position as:
        # 
        # [1, 3, 4] same char
        # 
        
        table1, table2 = collections.defaultdict(list), collections.defaultdict(list)
        
        for i in range(len(s)): table1[s[i]].append(i)
            
        for i in range(len(t)): table2[t[i]].append(i)
            
        table1_set = set([tuple(val) for key, val in table1.items()])
        table2_set = set([tuple(val) for key, val in table2.items()])
        return table1_set == table2_set