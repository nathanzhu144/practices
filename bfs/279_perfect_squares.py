
#  Nathan Zhu, Tuesday July 2nd, 2019, New York, Amex Building 36th floor, focus room
#  Leetcode 279 | medium | I think medium
import math
import collections

#  I like this question.
#  This is a hidden graph question.
#
#  So, when we are asking the fewest squares to make a number, we are
#  actually asking the shortest path between two nodes of a path...  Do a BFS
#  
#  Are cycles in this graph, so, makes sense to keep a visited set


def perfect_squares(num):
        # Generate all squares smaller or eq to num
    # does this from biggest -> smallest
    def smaller_squares(num):
        # for 26
        # 25, 16, 9, 4, 1
        ret = list()
        for i in range(int(math.sqrt(num)), -1, -1):
            ret.append(i ** 2)
        return ret

    if n == 0: return 0
    counter = 1
    visited = set()
    BFS = collections.deque([n])
    while BFS:
        BFS_next = list()
        for num in BFS:
            # neighbors should be all nodes 1 edge (1 square) away from num
            neighbors = [num - sq for sq in smaller_squares(num)]
            # we also want to check if each neighbor is visited
            # if it is visited, we don't add it to next
            for neighbor in neighbors:
                if neighbor == 0: return counter
                if neighbor not in visited:
                    BFS_next.append(neighbor)
                    visited.add(neighbor)
                    
        # we traversed another layer od nodes
        counter += 1
        BFS = BFS_next[:]
            

