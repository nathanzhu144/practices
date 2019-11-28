# # Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

#         0
#         |
#         1
#        / \
#       2   3 

# Output: [1]

# 1. It is only possible to have 2 minimum height trees roots at most.  
# 2. Suppose we pick any node in the tree.  Find the farthest node from that node, called "F1". "F1" is endpoint 
#    of a longest path. This is provable by contradiction.
# 3. We can do another BFS to find farthest node from "F1".  We find "F2".  "F1" and "F2" are endpoints of longest path
#    of this binary tree.  
# 4. Suppose length between "F1" and "F2" is odd. Midpoint is the MHT root.  If length between "F1" and "F2" is even,
#    then both of the midpoints are MHT roots.

# NOTE: When you are doing a BFS, make sure you put the beginning node in set, lmao.
#       Otherwise you can get wack results.

import collections
import copy




# def findMinHeightTrees(n, edges):
#     neighbors = collections.defaultdict(set)
#     for v, w in edges:
#         neighbors[v].add(w)
#         neighbors[w].add(v)
#     def maxpath(v, visited):
#         visited.add(v)
#         paths = [maxpath(w, visited) for w in neighbors[v] if w not in visited]
#         path = max(paths or [[]], key=len)
#         path.append(v)
#         return path
#     path = maxpath(0, set())
#     path = maxpath(path[0], set())
#     m = len(path)
#     return path[(m-1)/2:m/2+1]



##################################3
##       Perfect but TLE        ##
#################################
##  Damn, I wrote this and I was so happy, and it was basically perfect on the first try
#   My only logical mistake was not adding starting node to visited set, leading to a few 
#   weird edge cases, but it was so perfect :(
# 

#  This problem is minimizing diameter of a n-ary tree.  so, it is true that if you take any node and find the 
#  farthest node from that node, the node you find will be the endpoints of a longest-path
def minimum_height_tree_TLE(n, edges):
    
    # making graph dict track undirected edges of graph
    def connect(edges, graph):
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
    if not edges: return [0]

    # 1. init graph
    graph = collections.defaultdict(list)
    connect(edges, graph)

    # 2. Find  F1 by doing a BFS from a random node to farthest node.
    BFS = [0]
    visited = set([0])
    f1 = None

    # trying to figure out where to store f1
    while BFS:
        BFS_next = list()
        for node in BFS:
            # "farthest node we have seen so far"
            f1 = node
            # add neighbors to next
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    BFS_next.append(neigh)
        BFS = BFS_next[:]

    # 3. Let's find F2.  So, when we do F2 we want to find a midpoint, so to make the job easier, we make our BFS
    #    a BFS of queues instead of nodes.  Last node in each BFS is current node we are visiting, and cause we are
    #    doing a BFS, all lists in BFS should have equal length
    #
    # NOTE: A subtle issue here is neighbor issue.  If we add a neighbor to visited while iterating through a layer k,
    #       we can prune a path on the same layer k that also ends with the same neighbor  This is incorrect IF we are 
    #       trying to find all maximum paths but we only care about one, as both will be valid max paths.  However, we only
    #       need one max path, so it is OK.  This does become an issue if we use this idea in word ladder II, though.
    #       
    BFS = [[f1]]
    visited = set([f1])
    f1_to_f2paths = None
    while BFS:
        BFS_next = list()
        f1_to_f2paths = copy.deepcopy(BFS)
        for path in BFS:
            curr = path[-1]

            for neigh in graph[curr]:
                if neigh not in visited:
                    BFS_next.append(path + [neigh])

        # add neighbors here, even tho it doesn't matter, but this is approach in word ladder II
        for path in BFS_next: visited.add(path[-1])
        BFS = BFS_next # BFS and BFS_next point to same obj rn, but BFS_next goes outta scope, so BFS keeps reference

    # We return differently depending on whether even or odd
    # 0 1 2 3 4
    #     ^
    # 0 1 2 3
    #   ^ ^
    f1_to_f2_path = f1_to_f2paths[0]
    if len(f1_to_f2_path) % 2 == 1:
        return [f1_to_f2_path[len(f1_to_f2_path) // 2]]
    else:
        return [f1_to_f2_path[len(f1_to_f2_path) // 2 - 1]] + [f1_to_f2_path[len(f1_to_f2_path) // 2]]

    


    # do another BFS from "F1" to find "F2". Make this one a BFS of paths instead of a BFS of nodes.  
    # find midpoint between "F1" and "F2"

if __name__ == "__main__":
    # print(minimum_height_tree_TLE(2, [[0, 1]]))
    # print(minimum_height_tree_TLE(1, []))
    print(findMinHeightTrees(6,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))