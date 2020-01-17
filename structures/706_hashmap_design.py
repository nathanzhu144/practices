# Nathan Zhu 
# Leetcode 706 | easy | not so easy, some edge cases
# 
# This is a classic separate chaining linked list impl that keeps track of its load balance and rehashes at size > capacity.
# 
# Some tricks:
# - instead of using mod, I keep the size of the linked list a power of 2, and get the last couple
#   bits with a bitwise &.  Mods are expensive ops.
#
# 
# 


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.capacity = 2
        self.vec = [None, None]
        
    def grow(self):
        temp = self.vec[:]
        self.vec = [None] * (self.capacity * 2)
        self.capacity *= 2
        self.size = 0
        
        for bucket, node in enumerate(temp):
            curr = node
            while curr:
                self.put(curr.key, curr.val)
                curr = curr.next
            
        
    def put(self, key, value):
        bucket = key & (self.capacity - 1)
        
        n = Node(key, value)
        if self.vec[bucket] != None: 
            prev = None
            curr = self.vec[bucket]
            
            while curr:
                if curr.key == key:
                    curr.val = value
                    return
                prev = curr
                curr = curr.next
            prev.next = n
        else:
            self.vec[bucket] = n
        
        self.size += 1
        if self.size > self.capacity: self.grow()

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket = key & (self.capacity - 1)
        
        curr = self.vec[bucket]
        while curr:
            if curr.key == key: return curr.val
            curr = curr.next
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        bucket = key & (self.capacity - 1)
        
        curr = self.vec[bucket]  
        prev = None
        
        if not curr: return
        if curr.key == key:
            self.vec[bucket] = curr.next
            self.size -= 1
            return
            
        while curr:
            if curr.key == key:
                self.size -= 1
                prev.next = curr.next
            prev = curr
            curr = curr.next