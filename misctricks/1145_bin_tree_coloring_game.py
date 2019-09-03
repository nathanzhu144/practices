# Nathan Zhu August 27th, 2019, 2:09 pm 
# Leetcode 1145 | medium | 
# Category: brainteaser/misc tricks
# Done in real-time in a "Google on-site interview", 1 hour 59 min spent for 2 hour interview

# Then, the players take turns starting with the first player.  
# In each turn, that player chooses a node of their color 
# (red if player 1, blue if player 2) and colors an uncolored neighbor 
# of the chosen node (either the left child, right child, or parent of 
# the chosen node.)

def btreeGameWinningMove(self, root, n, x):
    """
    :type root: TreeNode
    :type n: int
    :type x: int
    :rtype: bool
    """
    # Choocse a value from 1 ... n
    # n cannot be equal to x.
    graph = collections.defaultdict(list)

    # Note that child is "current" node
    def make_graph(parent, child, graph_in):
        if parent and child:
            graph[parent].append(child)
            graph[child].append(parent)

        if child.left: make_graph(child, child.left, graph)
        if child.right: make_graph(child, child.right, graph)


    def find_x(root, x):
        if not root: return None
        if root.val == x: return root
        if root.val < x: return find_x(root.right, x)
        if root.val > x: return find_x(root.left, x)

    def find_area(curr, opponent, visited, graph):
        if curr in visited: return 0
        visited.add(curr)

        if curr == opponent: return 0

        area = 1
        for neighbor in graph[curr]:
            area += find_area(neighbor, opponent, visited, graph)

        return area

    make_graph(None, root, graph)
    start = find_x(root, x)
    areas = [find_area(neighbor, start, set(), graph) for neighbor in graph[start]]
    
    if not areas: return True
    
    return max(areas) > sum(areas) - max(areas)
