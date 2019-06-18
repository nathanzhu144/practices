#  Nathan Zhu 6:52 Amex building 200 Vessey street.  I've been trying to
#  debug this code for a few days now, and I finally understood the bug.  It was 
#  a simply mistake of not having two nested loops, so I was incrementing everytime
#  something was added to the queue
#  
#  
#  This question is a simple BFS question.
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
        BFS_current, BFS_next = [begin], list()

        visited = set()
        
        while BFS_current:
            while BFS_current:
                front = BFS_current.pop(0)

                if front in visited: 
                    continue
                    
                visited.add(front)
                
                if front == end:
                    return counter
                
                for i in range(len(front)):
                    for letter in alphabet:
                        new_word = front[:i] + letter + front[i + 1:]
                        if new_word in dictionary and new_word not in visited:
                            BFS_next.append(new_word)
                
            counter += 1
            BFS_current = BFS_next[:]
            BFS_next = list()               # If this line is not here, in cases where there is no valid word ladder -> infinite loop
                                            # as BFS_next (if anything is added to it) will never be empty, and then, BFS_current will never be empty
    return helper(beginWord, endWord, set(wordList))


if __name__ == "__main__":
    print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))