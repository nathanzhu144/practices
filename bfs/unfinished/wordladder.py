

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    def helper(begin, end, dictionary):
        alphabet = list(map(chr, range(97, 123)))
        counter = 0
        BFS = [begin]
        visited = set()
        
        while BFS:
            front = BFS.pop(0)

            if front in visited: 
                continue
                
            visited.add(front)
            
            if front == end:
                return counter
            
            for i in range(len(front)):
                for letter in alphabet:
                    new_word = front[:i] + letter + front[i + 1:]
                    if new_word in dictionary and new_word not in visited:
                        BFS.append(new_word)
            
            counter += 1
            
    return helper(beginWord, endWord, set(wordList))


if __name__ == "__main__":
    print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))