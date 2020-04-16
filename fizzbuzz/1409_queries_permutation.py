# Nathan Zhu April 11th, 2020. Stockton,  CA.  COVID-19
# Leetcode 1409 | medium | did not know to use a fenwick tree
# Category: Fenwick tree
# 


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LL:
    def __init__(self):
        self.fhead = Node(0)
        self.ftail = Node(0)
        self.fhead.next = self.ftail
        self.ftail.prev = self.fhead

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def append_front(self, node):
        node.next = self.fhead.next
        self.fhead.next.prev = node
        self.fhead.next = node
        node.prev = self.fhead

    def swap_front(self, node):
        self.remove(node)
        self.append_front(node)

    def count_pos(self, val):
        ret = 0
        curr = self.fhead.next
        while curr:
            if curr.val == val: return (curr, ret)
            ret += 1
            curr = curr.next
        return (None, -1)


class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        ret = []

        linked = LL()
        for i in range(m, 0, -1):
            linked.append_front(Node(i))

        for q in queries:
            node, idx = linked.count_pos(q)
            linked.swap_front(node)
            ret.append(idx)

        return ret