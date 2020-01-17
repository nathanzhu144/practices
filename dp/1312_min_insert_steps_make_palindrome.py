# Nathan Zhu Jan 6th, 2019 12:59 am Went to Alcatraz today!
# Leetcode 1312 | hard | not so bad
# Category: DP (like LPS)
#
# If you can understand longest palindromic subsequence, this is basically it but the costs are reversed.

def minInsertions(self, s):
    """
    :type s: str
    :rtype: int
    """
    table = dict()
    def helper(s, left, right):
        if left >= right: return 0
        key = (left, right)
        if key in table: return table[key]
        
        if s[left] == s[right]:
            table[key] = helper(s, left + 1, right - 1)
        else:
            table[key] = 1 + min(helper(s, left + 1, right), helper(s, left, right - 1))
        return table[key]
    
    return helper(s, 0, len(s) - 1)