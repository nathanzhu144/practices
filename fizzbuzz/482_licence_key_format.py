# Nathan Zhu September 3rd, 2019 2:48 pm
# Leetcode 482 | easy | annoying af
# Category: Fizzbuzz
# 
# Done in my only not-finished Google 1 hr online assessment.
# 

# You are given a license key represented as a string S which consists only alphanumeric
#  character and dashes. The string is separated into N+1 groups by N dashes. Given a number K, 
#  we would want to reformat the strings such that each group contains exactly K characters, 
#  except for the first group which could be shorter than K, but still must contain at least 
#  one character.  Furthermore, there must be a dash inserted between two groups and all
#  lowercase letters should be converted to uppercase.

# Input: S = "2-5g-3-J", K = 2

# Output: "2-5G-3J"

# Explanation: The string S has been split into three parts, each part has 2
#  characters except the first part as it could be shorter as mentioned above.



def licenseKeyFormatting(self, S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    l = S.replace("-", "")
    l = l.upper()
    
    front = len(l) % K
    
    ret = []
    
    ret.append(l[:front])
    if front != len(l) and front > 0: ret.append("-")
        
    while front < len(l):
        ret.append(l[front: front + K])
        front = front + K
        if front < len(l): ret.append("-")
        
    return "".join(ret)