# Nathan Zhu May 16th, 2020 Stockton, CA During weekly contest, man Q4 was a killer circle sweep line question
# Leetcode 1451 | medium | easy
# Category: fizzbuzz


def arrangeWords(self, text):
    """
    :type text: str
    :rtype: str
    """
    words = [word.lower() for word in text.split()]
    words.sort(key = len)
    if words:
        front = words[0]
        beginning = chr(ord(front[0]) - (ord('a') - ord('A')))
        words[0] = beginning + front[1:]
        
    return " ".join(words)