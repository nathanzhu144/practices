# /* Nathan Zhu Thursday, May 22nd, 2020 12:29 am, 3rd day at Salesforce just finished
# *  Leetcode 1021 | easy | think this should be medium
# *  Category: Misc tricks
# */



def removeOuterParentheses(s):
    """
    :type S: str
    :rtype: str
    """
    ret = []
    ctr = 0
    prev_s = 0
    for i, ch in enumerate(s):
        if ch == '(': ctr += 1
        else: ctr -= 1
        
        if ctr == 0:
            ret.append(s[prev_s + 1: i])
            prev_s = i + 1
            
    return "".join(ret)