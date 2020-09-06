# Nathan Zhu Monday July 27th, 2020 6:31 am, Stockton CA.  GOT POSITION #36/14309 for top 0.25% in Weely Contest 199.
#                                                          Last 2 weeks of SF internship.  :O  
# Leetcode 1307 | hard | deffo hard
# Category: backtracking with pruning
# Runtime: 10^N ??
# 
# Intution here.  Backtracking fully is really costly.
# We can do some smart pruning.
# If we go from the back, we can take the back digit for all of them.
# If the digits add up % 10 to not equal result digit, we can prune this possibility.
# Move N forward by 1 and repeat.

import collections



def isSolvable(words, result):
    """
    :type words: List[str]
    :type result: str
    :rtype: bool
    """
    concat = words + [result]
    N = max(map(len, concat))
    if concat[-1] < N: return False
    start_ch = set()
    for word in concat: 
        if word: start_ch.add(word[0])
    
    # linei : index in line of words
    # wordi : index in word
    # carry : carry from last addition
    # mapping: char -> num
    # used  : is a num used or not?
    def helper(linei, wordi, carry, mapping, used):
        if wordi == N: return carry == 0
        if linei == len(concat):
            sums = [mapping[word[-1 - wordi]] if wordi < len(word) else 0 for word in concat]
            tot = sum(sums) - sums[-1] + carry
            if tot % 10 != sums[-1]: return False
            carry = tot // 10
            return helper(0, wordi + 1, carry, mapping, used)
        
        # out of bounds on this word, move onto next word
        if wordi >= len(concat[linei]): return helper(linei + 1, wordi, carry, mapping, used)
        char = concat[linei][-1 - wordi]
        # char used before
        if char in mapping: return helper(linei + 1, wordi, carry, mapping, used)
        
        # This is to ensure no word starts with a 0.
        begin = 1 if char in start_ch else 0
        for i in range(begin, 10):
            if i in used: continue
            used.add(i)
            mapping[char] = i
            if helper(linei + 1, wordi, carry, mapping, used): return True
            del mapping[char]
            used.remove(i)
            
        return False
    
    return helper(0, 0, 0, {}, set())
