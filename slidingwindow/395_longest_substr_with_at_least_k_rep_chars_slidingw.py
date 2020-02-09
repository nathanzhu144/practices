# Nathan Zhu Feb 4th, 2020. Starbucks State Street 5:50 am  Have a phone call with ServiewNow today to see what happened in my interview.
# Leetcode 395 | medium | kinda hard?
# Category: Sliding window O(N)
# Note: There's a Divide and conq soln as well.
# 

# Insight 1: A alphabetical string can have at most 26 unique chars in it
#            (52) if we include upper case letters.
# Insight 2: We can find longest substring with at exactly m unique chars in O(N) time.
#
# Insight 3: While checking for longest substring with exactly m unique chars,
#            it is trivial to add a check that each of the m characters occurs at 
#            least k times.
#
# So, we go from 1, 2 .. 26 chars to see what is the l
# The trouble with this one is it is hard to figure out whether to close the window.
import collections
def longestSubstring(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    # This helper function will find the larger substring of k with 
    # exactly target_unique chars, where each of those target_unique chars
    # occurs at least k times.
    def helper(s, k, target_unique):
        c = collections.Counter()
        ret = 0
        left, right = 0, 0
        N = len(s)
        num_k = 0
        num_uni = 0

        while right < N:
            c[s[right]] += 1
            if c[s[right]] == k: num_k += 1
            if c[s[right]] == 1: num_uni += 1
            right += 1
            
            while left < right and num_uni > target_unique:
                c[s[left]] -= 1
                if c[s[left]] == k - 1: num_k -= 1
                if c[s[left]] == 0: num_uni -= 1

                left += 1
                
            if num_uni == target_unique and num_k == target_unique:
                ret = max(ret, right - left)
        return ret
    return max([helper(s, k, i) for i in range(1, 27)])

            
        
        