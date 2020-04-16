# Nathan Zhu Feb 15th, 2020.  My birthday.  We are at tea ninja doing practice exams for 376.  This is a damn cool question.  I figured this
#                             question out on my own.  This was on a practice 376 exam.
# Leetcode n/a | n/a | medium
# Category: DP, Minimax

# Given a graph, assuming that each node N has an outgoing edge to a larger numbered edge N'.  
# White and black take turns, and white starts on node 1. Whomever goes to the last node of the graph first wins.
# If white can guarantee a win, no matter what black does, return true.  
# 
# We just memoize on nodes (we revisit them)
# 

import collections
# Nodes are directed [1, 2] means Node 1 -> Node 2
def graph_game(nodes, start, dest):
    graph = collections.defaultdict(list)
    for a, b in nodes: graph[a].append(b)

    table = dict()
    def helper(n):
        if n == dest: return True  # whomever is on this node wins
        if n in table: return table[n]

        ret = True
        for neigh in graph[n]:
            ret = ret and not helper(neigh)

        return ret
    return helper(start)

if __name__ == "__main__":
    print(graph_game([[0, 1]], 0, 1))
    print(graph_game([], 0, 1))


