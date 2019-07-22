# Nathan Zhu, Sunday July 21st, 2019, 36th floor Amex Building.
# Leetcode 146 | medium | medium
# Category: data structure
# Question: Implement a LRU cache.
# 
# Note: Reads & writes are both accesses.
# 
# We use a double linked list with dict
# Order of DLL tracks least freq used, as least freq used is at end
# of DLL



# A large advantage of a doubly linked list is that a node can remove itself
# without any other references. Removal is constant time.
#
# Advantage of a pseudo-head and a pseudo-tail is that we don't need to check null
# node during an update

class Node:
    def __init__(self, key_in, val_in):
        self.key = key_in
        self.val = val_in
        self.prev = None
        self.next = None

class LRUCache(object):
    
    # Initial structure of DLL
    #       Dummyhead (next) ->     
    #                    <- (prev) Dummytail
    def __init__(self, capacity_in):
        """
        :type capacity: int
        """
        # Data structures #
        # self.table      - dictionary: key -> Node
        # self.capacity   - int: stores capacity for LRU
        # self.size       - int: stores current size of LRU
        # self.dummy_head - Node: ensures always prev node
        # self.dummy_tail - Node: tracks end of LL

        self.table = dict()
        self.capacity = capacity_in
        self.size = 0
        self.dummy_head = Node(0, 0)
        self.dummy_tail = Node(0, 0)
        self.dummy_tail.prev = self.dummy_head
        self.dummy_head.next = self.dummy_tail


    # O(1) runtime
    # Requires: None
    # Return  : val
    # Effects :
    #   1. "used", so move it to front of DLL
    #   2. returns value 
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.table: return -1
        ret = self.table[key].val
        self.move_to_head(self.table[key])
        return ret

    # O(1) runtime
    # Requires: None
    # Return  : None
    # Effects :
    #      If key already in DLL, we just modify value and move it to front of DLL,
    #      as it is "used"
    #     
    #      Otherwise, we make a new node, create a hash table entry, and increment size by 1.
    #      Then, we insert at front of DLL.  If inserting causes size to become bigger than
    #      capacity, we simply pop the tail off, deleting its hash table entry, and decrementing size by 1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.table.get(key)
        
        if not node:
            # 1. We insert first actual node (one after dummy_head)
            # 2. We insert the hash table entry for that node
            # 3. We increase size by 1
            new_node = Node(key, value)
            self.push_front_DLL(new_node)
            self.table[key] = new_node
            self.size += 1

            # 1. We remove the actual last node (one before dummy_tail)
            # 2. We delete the hash table entry for that node
            # 3. We decrease size by 1
            if self.size > self.capacity:
                del self.table[self.dummy_tail.prev.key]
                self.pop_tail()
                self.size -= 1
        else:
            #update the value
            node.val = value
            self.move_to_head(node)


    # O(1) runtime
    # Requires: None
    # Return  : None
    # Inserts node right after dummy head, before rest of elements
    # Links new node to after and dummy_head
    # Links after and dummy_head to new node
    def push_front_DLL(self, node_in):
        after = self.dummy_head.next
        
        node_in.prev = self.dummy_head
        node_in.next = after

        after.prev = node_in
        self.dummy_head.next = node_in
     
    # O(1) runtime
    # Requires: node in table
    # Return  : Node
    # Disconnects a node from DLL, does not delete it
    def remove_node(self, node):
        previous = node.prev
        after = node.next
        
        previous.next = after
        after.prev = previous
        
    # Moves a node from somewhere in DLL to front of DLL
    def move_to_head(self, node_in):
        self.remove_node(node_in)
        self.push_front_DLL(node_in)
    
    # Removess tail of DLL, returns Node
    def pop_tail(self):
        temp = self.dummy_tail.prev
        self.remove_node(temp)
        return temp