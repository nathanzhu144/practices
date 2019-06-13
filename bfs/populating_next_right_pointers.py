
# Nathan Zhu, Thursday June 13th, 2019, Amex Tower, 36th floor, New York
#
# The idea is to do a level order traversal of the tree.
# Store each level in a list, and iterate through the list
# connecting each list's next with the next one in the list.  The last item
# in the list has a next of nullptr
#
#                1  -> NULL
#        2    ->        3     -> NULL
#    4   ->   5   ->     6   ->   7    -> NULL
def connect(self, root):
    if not root:
        return None
    
    BFS_curr = [root]
    root.next = None
    BFS_next = list()
    
    while BFS_curr:
        while BFS_curr:
            front = BFS_curr.pop(0)
            
            if front.left:
                BFS_next.append(front.left)
            
            if front.right:
                BFS_next.append(front.right)
                
        for i in range(len(BFS_next)):
            if i + 1 < len(BFS_next):
                BFS_next[i].next = BFS_next[i + 1]
            else:
                BFS_next[i].next = None
                
        BFS_curr = BFS_next[:]
        BFS_next = list()
        
    return root