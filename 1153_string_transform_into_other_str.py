# Nathan Zhu January 4th, 2019
# Leetcode 1153 | medium | the edge cases are pretty interesting
# I thought this question was easy, but I didn't think about the case when len(set(str2)) == 26, then
# now I don't know if I fully understand the question.  It still seems pretty simple, but I don't
# understand some of the explanations.
# 
def canConvert(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: bool
    """
    # There are two major cases when we cases when a str1 cannot be converted into str2
    # 1. 
    #   The first case is when for a letter in str1, it is mapped to more than one charaacter
    #   in str2.  This is a problem because a group in str1 cannot be split up.
    #
    #   This is the obvious case.
    #
    # 2. 
    #   There, are 26 letters used up in str2.  
    #   Suppose there are only 3 letters in the alphabet.
    #  
    #   ["A", "B", "C"]
    #   
    #   Suppose we have a word like:
    #   s1 = "BAC", s2 = "ABC"
    #   Note that since "ABC" has all the characters in the alphabet, it is impossible to change "BAC" to ABC.
    #
    #   However, if there are 4 letters including "D" in the alphabet, we can do this:
    # 
    #   BAC ->  DAC -> DBC -> ABC
    #   
    # 
    
    if str1 == str2: return True
    # after this point, we definitely need to do conversions
    if len(set(str2)) == 26: return False                    # check to see if conversions are possible with s2
    
    table = dict()
    
    for i, j in zip(str1, str2):
        if table.setdefault(i, j) != j: return False
        
    return True

if __name__ == "__main__":
    canConvert("aabbcc", "ccddee")
    canConvert("leetcode", "codeleet")