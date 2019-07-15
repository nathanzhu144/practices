
##
#  Optimizations:
#     1. Unlike DFS where you may run into endless loops when the graph has cycles, BFS is a better tool.
#        However, simply having a visited set, where after you visit a node you put it in the visited set
#        is incredibly helpful.  Do not revisit nodes. Reduces runtime to O(V), I think, because we can at most visit all vertices.
# 
#        There is a proof in the 203 textbook about why a path that reaches same node twice is shorter.
#        Gist is that there exists a cycle that can be pruned. 
#
#      2. Two-ended BFS can be a substantial optimization.  The idea is that if the branching factor is B,
#         and distance of search is D, it is likely that D^(B/2) + D^(B/2) < D^B.
#         So, in the word ladder, we would start with beginning and end word, and if any of the words found by beginning
#         were same as any word found in end, we have found where they meet.
#      
#  Mistakes made: 
#     1. Not having inside loop.  So, kept counting everytime I explored a new edge.  You only increment when
#        you add a new "level" of nodes.
#
#     2. Not resetting BFS_next to empty list.  This results in an infinite loop when we cannot find the end word.
#
#  
#     
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
        BFS_current = [begin]

        visited = set()                     # Reduces runtime to O(V), as we at most visit V vertices.
        
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