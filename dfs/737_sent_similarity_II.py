# Nathan Zhu August 30th, 2019 10:55 pm
# Leetcode 737 | medium | not bad
# Category: BFS
#
# Done in a mock google on-site interview
# Your interview score of 5.54/10 beats 87% of all users.
# Time Spent: 1 hour 51 minutes 22 seconds
# Time Allotted: 2 hours

# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if 
# two sentences are similar.
#
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs 
# are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].
#
# Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, 
# then "great" and "fine" are similar.
#
# Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar,
# even though there are no specified similar word pairs.
#
# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be
#  similar to words2 = ["doubleplus","good"].



Google- On-Site Interview
CompletedAugust 30, 2019 10:55 PM
87%
Your interview score of 5.54/10 beats 87% of all users.
Time Spent: 1 hour 51 minutes 22 seconds
Time Allotted: 2 hours


class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        
        def bfs(word1, target, similar):
            visited = set()
            
            q = [word1]
            while q:
                nextq = []
                for i in range(len(q)):
                    currword = q[i]
                    if currword == target: return True
                    
                    for neighbor in similar[currword]:
                        if neighbor not in visited:
                            nextq.append(neighbor)
                            visited.add(neighbor)                
                q = nextq
            return False
        
            
        if len(words1) != len(words2): return False
        
        similar = collections.defaultdict(list)
        for p1, p2 in pairs:
            similar[p1].append(p2)
            similar[p2].append(p1)
            
        
        for i in range(len(words1)):
            if words1[i] != words2[i]:
                if not bfs(words1[i], words2[i], similar): return False
                
        return True