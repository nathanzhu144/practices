# Nathan Zhu Wednesday Nov 20th, 2019.  6:32 am Duderstadt baseement.  Going to salesforce.
# Leetcode 1192 | hard | yeah pretty hard
# Category: DFS (tarjan's algorithm)
# Runtime : O(V + E) time, O(V + E) space

# 
# Intuition:
# An edge is a critical edge if and only if it is not in a cycle.  
#
# Therefore, if we can detect all edges in a cycle, and delete all edges in a cycle, 
# we are left with all the critical edges.
#
# To do this: 
# 1. We do a DFS and keep track of the level/depth of the recursion at each step. 
#    Suppose that during the recursion we visit a neighbor that has was found at a depth
#    smaller than N, then we have a cycle. We can keep track of the depths of all nodes
#    we have seen before in an array. Unseen nodes will have a depth value of -2.
#
#    (Note, to make sure we don't recurse back to parent immediately, before
#     going to a neighbor node, we make sure neighbor's depth is not currentdepth - 1)
#
#
# 2. DFS returns the minimum depth it has "seen" so far among all its neighbors.
#    Suppose we have currenot node (A) and neighbor (B).
#    If DFS(B) <= level of A, it means that A or one of A's ancestors eventually
#                             link with B's descendants.
#
#
#            F (depth = 5) ->  C (depth = 2) <- B (depth = 1)  <- A (depth = 0)
#            ^                 |
#            |                 v
#            E (depth = 4) <-  D (depth = 3)
#  
#            The arrows denote a possible DFS path.
# 
#            We delete (A, D) return min depth of 2
#            We delete (E, F) return min depth of 2
#            We delete (D, E) return min depth of 2
#            We delete (C, D) return min depth of 2
#            We keep (B, C) as returned 2 > B's level of 1
#            We keep (A, B) as returned 1 > A's level of 0


import collections

def criticalConnections(n, connections):
    def make_graph(connections):
        graph = collections.defaultdict(list)
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
        return graph

    level_found = [-2] * n   # all un-visited nodes are initted as level -2
                             # this DS keeps tracks of the levels of nodes we have seen before

    graph = make_graph(connections)
    connections = set(map(tuple, map(sorted, connections)))

    def dfs(curr_node, level):
        # We have seen this node before.
        if level_found[curr_node] >= 0: return level_found[curr_node]

        min_level_found = level
        level_found[curr_node] = level

        for neigh in graph[curr_node]:
            if level_found[neigh] == level - 1: continue             # do not visit immediate parent.

            smallest_depth_from_this_neigh = dfs(neigh, level + 1)   # if we visit this neighbor, what's smallest level we can get to?
            
            if smallest_depth_from_this_neigh <= level:              # if by following this neighbor, we get to smaller or equal level, 
                connections.remove(tuple(sorted(curr_node, neigh)))  # this (node, neighbor) eventually leads to a cycle.  Remove this.

            min_level_found = min(smallest_depth_from_this_neigh, min_level_found)  # find smallest level we can get to from all neighbors.
        return min_level_found

    dfs(0, 0)                 # we assume this is a connected graph, so we don't need to run through all edges.
    return list(connections)






        
    dfs(0, 0)  # since this is a connected graph, we don't have to loop over all nodes.
    return list(connections)


if __name__ == "__main__":
    criticalConnections(8, [[0,1],[1,2],[2,0],[1,3],[3, 4], [4,6], [4,5], [5, 6]])
