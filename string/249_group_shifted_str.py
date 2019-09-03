#  Nathan Zhu August 31st, 2019, 2:24 am
#  Leetcode 249 | medium | not too bad...
#  Google on-site interview 
#  Your interview score of 3.21/10 beats 48% of all users.
#  Time Spent: 1 hour 59 minutes 14 seconds
#  Time Allotted: 2 hours

#  Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
#
# Example:
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output: 
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        
        def is_match(str1, str2):
            if not str1 and not str2: return True
            
            lastdiff = (ord(str1[0]) - ord(str2[0])) % 26
            for i in range(len(str1)):
                if (ord(str1[i]) - ord(str2[i])) % 26 != lastdiff: return False
                
            return True
            
            
        # We have a mapping from len of str -> list of different strings (each with own set)
        # [abc, [abc, def, xyz]]
        table = collections.defaultdict(list)
        
        for string in strings:
            hasmatch = False
            for pattern, patternlist in table[len(string)]:
                if is_match(pattern, string):
                    hasmatch = True
                    patternlist.append(string)
                    
            if not hasmatch:
                table[len(string)].append([string, [string]])
        
        ret = []
        for key, val in table.items():
            for pattern, patternlist in val:
                ret.append(patternlist)
                
        return ret