# Nathan Zhu, Sunday August 4th, 5:13 am.  EHS 55 John Street.  My roommate just had sex very loudly and I couldn't
#                                          fall asleep, 
# Leetcode 340 | hard | not too bad, classic sliding window problem for strings
# Runtime: O(N)
# Category: String sliding window
import collections

def lengthOfLongestSubstringKDistinct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    # Datastructures #
    # table maps   char -> num occurrences
    # rightidx, leftidx are inclusive of current string
    # uniqcounter is number of unique characters in current string
    # ret is max length seen so far.
    table = collections.defaultdict(int)
    rightidx = 0                     
    leftidx = 0
    uniqcounter = 0
    ret = float('-inf')
    if not s or not k: return 0
    
    while rightidx < len(s):
        # Check to see if we have encounted a new character
        if table[s[rightidx]] == 0:
            uniqcounter += 1
        table[s[rightidx]] += 1
        
        while leftidx < rightidx and uniqcounter > k:
            table[s[leftidx]] -= 1
            # Check to see if we have lost a unique character
            if table[s[leftidx]] == 0:
                uniqcounter -= 1
            # BE CAREFUL WHERE THIS PLACED
            leftidx += 1

        # At this point uniqcounter <= k
        ret = max(ret, rightidx - leftidx + 1)
        # BE CAREFUL WHERE THIS PLACED
        rightidx += 1
        
    return ret

if __name__ == "__main__":
    print(lengthOfLongestSubstringKDistinct("bacc", 2))