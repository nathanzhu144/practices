# Nathan Zhu Monday Nov 25th, 2019 12:50 pm
# Leetcode 953 | easy | easy
# Category: Sorting
    

# While it is hard to actually use the alien dictionary, if we map the alien dict to numbers,
# and then replace the chars with numbers, we can use string comparison with everything.

# Runtime is O(N), where N is the number of characters in all the words combined.

def isAlienSorted(words, order):
    """
    :type words: List[str]
    :type order: str
    :rtype: bool
    """
    table = dict()
    new_words = list()

    for c in range(26):
        table[order[c]] = c
        
    for w in words:
        new_word = []
        for c in w:
            new_word.append(table[c])
        new_words.append(new_word)
    
    # We can check if new_words is sorted now.
    for w1, w2 in zip(new_words, new_words[1:]):
        # Same prefix,  but word2 is shorter.
        if len(w1) > len(w2) and w1[:len(w2)] == w2: return False
        for c1, c2 in zip(w1, w2):
            if c1 < c2: break
            if c2 < c1: return False
    return True

if __name__ == "__main__":
    print(isAlienSorted(["wo","w"], "worldabcefghijkmnpqstuvxyz"))