# Nathan Zhu Monday September 9th, 2019 5:25 pm, 3 days until microsoft phone screen
# Leetcode 432 | hard | yeah damn hard
# https://leetcode.com/problems/all-oone-data-structure/discuss/91428/Python-solution-with-detailed-comments
# 
# All O(1) data structure, where 4 operations are supported.
# Incrementing a key (incrementing key if there is one, otherwise makes one with a count of 1)
# Decrementing a key (and removing it if no such key)
# Getting maximum, return "" if no max
# Getting minimum, return "" if no min

# Data structures
# Each node has a key set, a set of keys.  The idea behind a node is a node represent ALL KEYS WITH THAT FREQUENCY.
# And, the nodes in the DLL should have an increasing frequency:
#      - First (after sentinal at front) node represents things with smallest count
#      - Last (before sentinal at end) holds all keys with largest count
#      - Front sentinal representing things with 0 frequency
#
# self.key_counter   maps a key -> count
# self.freq_to_node  maps a freq -> a Node in DLL
# self.DLL is internal DLL


# General algorithm
# When we increment:
#  1. We check inside key_counter to see if this key is inside our data structure.
#     - If it is, we use freq_to_node to get our key.
#     - If not, we make a new node, and insert it in.
#
#  2. We add key into our node with a higher count.
#  3. We decrement key into previous node with a smaller count.

# When we decrement:
#  1. We check inside key counter to see if this key is inside our DS
#  2. We add key to node with smaller count (count - 1).
#  3. We decrement key in previous node.

# When we get biggest:  Get node after back sentinal
# when we get smallest: Get node after front sentinal
import collections
class Node(object):
    def __init__(self):
        self.key_set = set()
        self.prev, self.next = None, None

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)

    def get_any_key(self):
        if not self.key_set: return None

        ret = self.key_set.pop()
        self.add_key(ret)
        return ret
    
    def count(self):
        return len(self.key_set)

    def empty(self):
        return len(self.key_set) == 0


class DoublyLinkedList(object):
    def __init__(self):
        self.sentinal_head, self.sentinal_tail = Node(), Node()
        self.sentinal_head.next, self.sentinal_tail.prev = self.sentinal_tail, self.sentinal_head

    # Makes a new empty node, inserts it after node X, and returns a ref to that node
    def insert_after(self, x):
        previous, newnext = x, x.next
        newnode = Node()
        previous.next = newnode
        newnext.prev = newnode

        newnode.next = newnext
        newnode.prev = previous
        return newnode

    def insert_before(self, x):
        return self.insert_after(x.prev)

    def remove(self, x):
        prev_node, next_node = x.prev, x.next
        prev_node.next, next_node.prev = next_node, prev_node

    def get_head(self):
        return self.sentinal_head.next
    def get_tail(self):
        return self.sentinal_tail.prev
    def get_sentinal_head(self):
        return self.sentinal_head

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll, self.key_counter = DoublyLinkedList(), collections.defaultdict(int)
        self.freq_to_node = {0: self.dll.get_sentinal_head()}

    # Handles removing key from a node.  If there are no more keys in this node's set, we delete the node
    def remove_key_pf_node(self, pf, key):
        node = self.freq_to_node[pf]
        node.remove_key(key)
        if node.empty():
            self.dll.remove(node)
            self.freq_to_node.pop(pf)


    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        self.key_counter[key] += 1
        cf, pf = self.key_counter[key], self.key_counter[key] - 1

        # We check to see if a bucket exists for the bigger counter value of cf.  If not, we make one and insert it after
        if cf not in self.freq_to_node:
            self.freq_to_node[cf] = self.dll.insert_after(self.freq_to_node[pf])
        self.freq_to_node[cf].add_key(key)

        # if pf is 0, it is the sentinal node, so we don't need to remove key from previous node
        if pf > 0: self.remove_key_pf_node(pf, key)


    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key not in self.key_counter: return

        self.key_counter[key] -= 1
        cf, pf = self.key_counter[key], self.key_counter[key] + 1

        if self.key_counter[key] == 0: self.key_counter.pop(key)

        # If cf is 0, we don't need to move the key down to the previous bucket, as 
        # cf of 0 represents the sentinal head.  
        if cf != 0:
            # We check to see if a bucket exists for the smaller counter value of cf.  If not, we make one and insert it before
            if cf not in self.freq_to_node:
                self.freq_to_node[cf] = self.dll.insert_before(self.freq_to_node[pf])
            self.freq_to_node[cf].add_key(key)
        self.remove_key_pf_node(pf, key)
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.dll.get_tail().get_any_key() if not self.dll.get_tail().empty() else ""
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.dll.get_head().get_any_key() if not self.dll.get_head().empty() else ""


if __name__ == "__main__":
    a = AllOne()
    a.inc(1)
    print(a.getMaxKey())
    print(a.getMinKey())
