#  Nathan Zhu New York, 12:25 pm, Amex Tower
#  Leetcode 133 medium | I think medium
#   We first do a BFS, and make a hash table that maps
#      Node in original ->  Deep copy of node in original
# 
#   Then, we iterate through a second time
#      table[original_node]     
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
#   
#
#   Original Graph
#          A -----  B
#         -
#        -
#       C          
# 
#   We first do a BFS, and make a hash table that maps
#      Node in original ->  Deep copy of node in original
# 
#   Then, we iterate through a second time
#   for node in curr.neighbors:
#      table[curr].neighbors.append(table[node])
#
#   Then, we have created a deep copy.  See explanation of copying
#   a linked list with next and random pointers for better explanation
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

    def add_neighbor(self, node):
        self.neighbors.append(node)



def cloneGraph(self, node):
    """
    :type node: Node
    :rtype: Node
    """
    if not node:
        return None
    
    temp = node
    BFS_curr = [temp]
    BFS_next = list()
    node_to_copy = dict()
    visited = set()
    
    while BFS_curr:
        while BFS_curr:
            head = BFS_curr.pop(0)
            
            if head in visited:
                continue
            visited.add(head)
            
            for i in head.neighbors:
                BFS_next.append(i)
            
            node_to_copy[head] = Node(head.val, [])
        BFS_curr = BFS_next[:]
        BFS_next = list()
    
    temp = node
    BFS_curr = [temp]
    BFS_next = list()
    visited.clear()
    
    while BFS_curr:
        while BFS_curr:
            head = BFS_curr.pop(0)
            
            if head in visited:
                continue
            visited.add(head)
            
            for i in head.neighbors:
                BFS_next.append(i)
            
            for nod in head.neighbors:
                node_to_copy[head].neighbors.append(node_to_copy[nod])
                
        BFS_curr = BFS_next[:]
        BFS_next = list()
    
    return node_to_copy[node]

if __name__ == "__main__":
    n1 = Node(1, [])
    n2 = Node(2, [])
    n1.add_neighbor(n2)
    n2.add_neighbor(n1)
    cloneGraph(n1)