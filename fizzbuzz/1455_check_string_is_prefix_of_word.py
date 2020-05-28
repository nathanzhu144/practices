# Nathan Zhu Stockton, CA. May 23rd, 2020.  Watched lights out today with Rak and Neha
# Leetcode 1455 | easy | easy
# Categry: fizzbuzz

def isPrefixOfWord(sentence, searchWord):
    """
    :type sentence: str
    :type searchWord: str
    :rtype: int
    """
    arr = sentence.split(" ")
    for i, a in enumerate(arr):
        if a.startswith(searchWord): return i + 1
    return -1