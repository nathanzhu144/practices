# Nathan Zhu August 30th, 2019 10:55 pm
# Leetcode 734 | easy | EZ
# Category: Misc
# Done in a mock google on-site interview
# Your interview score of 5.54/10 beats 87% of all users.
# Time Spent: 1 hour 51 minutes 22 seconds
# Time Allotted: 2 hours

# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs,
# determine if two sentences are similar.  For example, "great acting skills" and "fine drama talent" are similar, if 
# the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].
#
# Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and
# "good" are similar, "great" and "good" are not necessarily similar.
#
# However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.
#
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], 
# pairs = [] are similar, even though there are no specified similar word pairs.
#
# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can
# never be similar to words2 = ["doubleplus","good"].

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        
        
        similar = collections.defaultdict(list) 
        for first, sec in pairs:
            similar[first].append(sec)
            similar[sec].append(first)
            
        
        for i in range(len(words1)):
            if words1[i] != words2[i]:
                if words2[i] not in similar[words1[i]]: return False
        
        return True