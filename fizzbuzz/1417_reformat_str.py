# Nathan Zhu April 19th, 2020. Stockton, CA Weekly contest 185, position 225 / 9206, a bit above top 2.5%.  First contest to get all 4 qs, also no WAs.
# Leetcode 1417 | easy | EZ
# Category: fizzbuzz 
# 
def reformat(self, s):
    """
    :type s: str
    :rtype: str
    """
    nums, letters = [], []
    for ch in s:
        if "0" <= ch <= "9": nums.append(ch)
        else: letters.append(ch)
            
    # first is majority or eq
    def helper(fir, sec):
        ret = []
        if len(fir) < len(sec):
            return helper(sec, fir)
        
        while fir or sec:
            if fir: ret.append(fir.pop())
            if sec: ret.append(sec.pop())
        
        return ret

    if abs(len(nums) - len(letters)) > 1: return ""
    return "".join(helper(nums, letters))