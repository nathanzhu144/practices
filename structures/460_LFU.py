# Nathan Zhu 6:56 am Starbucks coffee State Street
# Leetcode 460 | hard | yeah hard
#
# We want a LFU cache, that tie-breaks with a LRU cache.
# 
import collections
class Node(object):
    def __init__ (self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLL(object):
    def __init__(self):
        self.size = 0
        self.d_head, self.d_tail = Node(0, 0), Node(0, 0)
        self.d_head.next = self.d_tail
        self.d_tail.prev = self.d_head

    def __len__(self):
        return self.size

    # Appends to front of the DLL
    def append(self, node):
        oldnext = self.d_head.next
        node.next = oldnext
        node.prev = self.d_head

        self.d_head.next = node
        oldnext.prev = node

        self.size += 1

    # Pops from back of DLL by default
    def pop(self, node = None):
        # This prevents the deletion of dummyhead if size == 0
        if self.size == 0: return
        if not node: node = self.d_tail.prev

        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1
        return node

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        
        # Important DS and variables #
        self.table = dict()                              # maps key to its node
        self.freq = collections.defaultdict(DLL)         # maps a node to its DLL
        self.min_freq = 1                                # minimum frequency (for eviction)

    def update(self, node):
        freq = node.freq

        self.freq[freq].pop(node)

        if self.min_freq == freq and len(self.freq[freq]) == 0:
            self.min_freq += 1

        node.freq += 1
        newfreq = node.freq
        self.freq[newfreq].append(node)


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.table: return -1

        node = self.table[key]
        self.update(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # this is a strange edge case
        if self.capacity == 0: return 

        if key in self.table:
            node = self.table[key]
            node.val = value
            self.update(node)
        else:
            # We need to evict now
            # Asssume size >= 1
            if self.size == self.capacity:
                evicted = self.freq[self.min_freq].pop()
                del self.table[evicted.key]
                self.size -= 1
            
            node = Node(key, value)
            self.table[key] = node
            self.size += 1
            self.freq[1].append(node)
            self.min_freq = 1


if __name__ == "__main__":
    n = LFUCache(2)
    n.put(3, 1)
    n.put(2, 1)
    n.put(2, 2)
    n.put(4, 4)
    print(n.get(2))

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)