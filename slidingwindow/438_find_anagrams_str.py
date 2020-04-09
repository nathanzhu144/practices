# Nathan Zhu 11:19 pm Christmas Dec 25th, 2019, eating dinner
# Nathan Zhu April 9th, 2020, 12:22 am, COVID-19
# Leetcode 438 | medium | medium
# Category: Sliding window
# Runtime: O(N)

import collections

def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    left, right = 0, 0
    anagram = collections.Counter(p)
    counter = 0
    ret = []
    
    # cba
    #    ^
    #   
    while right < len(s):
        if s[right] in anagram:
            anagram[s[right]] -= 1
            if anagram[s[right]] == 0: 
                counter += 1
        right += 1
        
        # when we have the proper number of each letter,
        # we have a correct position
        if counter == len(anagram):
            ret.append(left)
        
        if right - left >= len(p):
            if s[left] in anagram:
                anagram[s[left]] += 1
                if anagram[s[left]] == 1: 
                    counter -= 1
            # only increment left ptr when sliding window gets to size of word
            left += 1
    return ret

if __name__ == "__main__":
    print(findAnagrams("acbdpabce", "abc"))
