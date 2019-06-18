import collections


def findladder(begin_word, end_word, wordlist):
    wordlist = set(wordlist)
    returned = []
    BFS_curr = dict()
    BFS_curr[begin_word] = [[begin_word]]

    while BFS_curr:
        BFS_next = collections.defaultdict(list)
        for curr_word in BFS_curr:
            if curr_word == end_word:
                returned.extend(k for k in BFS_curr[curr_word])
            else:
                for i in range(0, len(curr_word)):
                    for c in string.ascii_lowercase:
                        new_word = curr_word[:i] + c + curr_word[i + 1:]
                        if new_word in wordlist:
                            BFS_next[new_word] += k + [new_word] for k in BFS_curr[curr_word]
            
        wordlist -= set(BFS_next.keys())
        BFS_curr = BFS_next
    return returned
                    























def findLadders(beginWord, endWord, wordList):

    wordList = set(wordList)
    res = []
    layer = {}
    layer[beginWord] = [[beginWord]]

    while layer:
        newlayer = collections.defaultdict(list)
        for w in layer:
            if w == endWord: 
                res.extend(k for k in layer[w])
            else:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        neww = w[:i]+c+w[i+1:]
                        if neww in wordList:
                            newlayer[neww] += layer+[neww] for j in layer[w]]

        wordList -= set(newlayer.keys())
        layer = newlayer

    return res

if __name__ == "__main__":
    print(findLadders("hit","cog", ["hot","dot","dog","lot","log","cog"]))
