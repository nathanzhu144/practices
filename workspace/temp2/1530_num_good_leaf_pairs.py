# Nathan Zhu Saturday July 26th, 2020, Stockton CA.  GOT POSITION #36/14309 for top 0.25% in Weely Contest 199.
# I honestly never thought I'd get that high in the next year or next few years.  I only thought it would take
# a few years, and for me to start competitive programming in earnest to actually get that good.  I got 300 leetcode 
# points.  :)  
#
# There wasn't anything super special in Q1 - Q3.
# Q1 took 2 min cuz I was 1 minute late in starting                     (+2:26 min, total 2:26)
# Q2 was an O(N) greedy bit flip question, where it is easy to write the algorithm if you have the idea, but
#    hard to prove why it would work.                                   (+7:45 min, total 10:16)
#                                  ]
# Q3 probably had a really smart solution, probably binary lifting with LCA, the question was how many leaf pairs
# were k distance apart.  I did brute force BFS from each leaf, and then dividing by two for total.
#                                                                       (+20:03 min, total: 30:19)
# Q4 was why I did well.  I'm strongest on DP and graph problems, weak on probability, geometry, etc.   
# I knew I could finish all the problems when I saw this problem, but I think I was overconfident.
# Halfway through trying to memoize with 2D DP, I realized I needed another 2 variables in the 
# memoization for it to work out properly.  So, I ended up with a 4D DP problem.
# I was initially skeptical, but couldn't see a better way, so I kept at it. 
#
# Extremely lucky on Q4 not to have any wrong submissions.  Even william lin had like 2 submission failures. 
# I caught the case where we have to increase RLE by 1 if we go from 9->10 and 99->100
# 
# I initially saw the score, before me finishing Q4, and I was position #600 or so, and I was kinda sad that finishing all 4
# gave my such a low position, but it turned out that my Q4 submission didn't update yet, and I went from #600 -> #36.
#
# 10 minutes slower than William Lin.  I'm super happy w that, but I definitely have room for improvements.  
#                                                                       (+20:12 min, total: +50:31)
#
# Good finish this time, but need more work for future.
#
# Leetcode: 1530 | medium | medium
# Category: Tree
# Runtime:  O(N^2)
# Just did a BFS from each leaf node to each other leaf node within k distance.
# One change I thought was smart was I didn't keep a hash table to avoid double counting, I just divide by 2.
# If leaf node  A can reach leaf node B, B can also each A.
# 
import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countPairs(self, root, distance):
    """
    :type root: TreeNode
    :type distance: int
    :rtype: int
    """
    leaves = set()
    graph = collections.defaultdict()
    if not root or (not root.left and not root.right): return 0
    
    # gets all leaves
    def get_leaves(root):
        if not root: return
        if not root.left and not root.right: 
            leaves.add(root)
        get_leaves(root.left)
        get_leaves(root.right)
        
    # connects graph
    def make_graph(root, parent):
        if not root: return
        if parent and root:
            #print(root.val, parent.val)
            if parent not in graph: graph[parent] = []
            if root not in graph: graph[root] = []
            graph[parent].append(root)
            graph[root].append(parent)
        make_graph(root.left, root)
        make_graph(root.right, root)
        
    def BFS(root, k):
        q = collections.deque([root])
        visited = set([root])
        ret = 0
        if k == 0: return 0
        while q:
            currlen = len(q)
            for i in range(currlen):
                curr = q.popleft()
                for neigh in graph[curr]:
                    if neigh in visited: continue
                    visited.add(neigh)
                    if neigh != root and neigh in leaves: ret += 1
                    q.append(neigh)
            k -= 1
            if k == 0: break
                
        return ret
                
    get_leaves(root)
    make_graph(root, None)
    ret = 0
    for leaf in leaves: ret += BFS(leaf, distance)
            
    return ret // 2