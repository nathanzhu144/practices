# Nathan Zhu September 5, 2019 8:54 PM
# Leetcode 165 | medium | EZ
# Category: Fizzbuzz
# Microsoft- Phone Interview (leetcode)
# Your interview score of 6.73/10 beats 82% of all users.
# Time Spent: 30 minutes 41 seconds
# Time Allotted: 1 hour 30 minute

# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1; otherwise return 0.

# You may assume that the version strings are non-empty and contain only digits and the . character.

# The . character does not represent a decimal point and is used to separate number sequences.

# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth 
# second-level revision of the second first-level revision.

# You may assume the default revision number for each level of a version number to be 0. For example,
#  version number 3.4 has a revision number of 3 and 4 for its first and second level revision number.
#   Its third and fourth level revision number are both 0.

def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1 = version1.split(".")
    v2 = version2.split(".")
    
    i = 0
    while i < len(v1) or i < len(v2):
        curr1, curr2 = 0, 0
        if i < len(v1): curr1 = int(v1[i])
        if i < len(v2): curr2 = int(v2[i])
            
        if curr1 < curr2: return -1
        elif curr1 > curr2: return 1
        i+= 1
        
    return 0