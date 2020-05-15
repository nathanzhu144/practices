# Nathan Zhu, April 4th, 2020, Just finished 376 final, woooooo, got above median, Meera's bday yesterday.
# Leetcode 127 | medium | medium
# Category: BFS
# This is an oldie but a goodie. "the classic bfs problem"
import string

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    dictionary = set(wordList)
    q = [beginWord]
    ret = 1
    
    while q:
        newq = []
        for item in q:
            if item == endWord: return ret
            for i in range(len(item)):
                for ch in string.ascii_lowercase:
                    newword = item[:i] + ch + item[i + 1:]
                    if newword not in dictionary: continue
                    print(newword)
                    dictionary.remove(newword)
                    newq.append(newword)
        q = newq
        ret += 1
        
    return 0