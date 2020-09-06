# /* Nathan Zhu Wednesday, Stockton, CA. 12:11 am, June 18th, 2020.  Tomorrow is our 2nd anniversary. :)  Also, about to hit 50% of questions done on LC today.  49.9% rn!
# *  Leetcode 678 | medium | kinda harad
# *  Category: stack
# */


def checkValidString(self, s):
    """
    :type s: str
    :rtype: bool
    """
    left_s, star_s = [], []
    for i, ch in enumerate(s):
        if ch == "(": left_s.append(i)
        if ch == "*": star_s.append(i)
        if ch == ")":
            if not star_s and not left_s: return False
            if not left_s: star_s.pop()
            else: left_s.pop()
                
    while left_s:
        if not star_s: return False
        if left_s.pop() > star_s.pop(): return False
        
    return True