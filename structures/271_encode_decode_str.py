# Nathan Zhu Feb 10th, 2020.  In silly humanities class.
# Leetcode 271 | medium | cool one
# Category: Design / Misc tricks

# This is pretty smart IMO.
# We double hashes inside the strings, then use standalone hashes inside the string to 
# mark string endings. 
#
# For example:
# ["abc##", "#def"]   ->   "abc#### # ##def"
# ["abc", "def", "g"] ->   "abc # def # g"
# [""] gets encoded to " # "
# [] get encoded to ""
# 
# Explanation, splitting " # " gets us the array ["", ""],
# We iterate up to, but not including last element, so returned string is [""]
#
# Splitting "" gets us the array [""]
# We iterate up to, but not including last element, so return []


class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        ret = []
        for i, string in enumerate(strs):
            for ch in string:
                if ch == "#": ret.append("##")
                else: ret.append(ch)
                    
            ret.append(" # ")
            
        fin = "".join(ret)
        print(fin)
        return fin

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ret = []
        temp = s.split(" # ")
        for j in range(len(temp) - 1):   # We DO NOT INCLUDE the last element.
            currstr = []
            string = temp[j]
            
            i = 0
            while i < len(string):
                if string[i: i + 2] == "##": 
                    currstr.append("#")
                    i += 2
                else:
                    currstr.append(string[i])
                    i += 1
                    
            ret.append("".join(currstr))
        return ret
                