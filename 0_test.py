
import collections
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # left, right
    l, r = 0, 0
    table = collections.defaultdict(int)
    duplicated = 0
    N = len(s)
    ret = 0
    # A B C A B C?
    # L R           R
    # 0 1 2 3 4 5 
    # 
    # B A B G
    # 0 1 
    # L L   R

    while r < N:
        table[s[r]] += 1
        if table[s[r]] > 1: duplicated += 1
        r += 1
        
        while l + 1 < r and duplicated >= 1:
            table[s[l]] -= 1
            if table[s[l]] == 1: duplicated -= 1
            l += 1
        ret = max(ret, r - l)
    return ret

if __name__ == "__main__":
    print(lengthOfLongestSubstring("bbb"))