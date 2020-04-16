# Nathan Zhu May 30th, 2020.  Foundry Lofts, COVID-19
# Leetcode 631 | hard | hard
# Category: Design

import collections

class Excel(object):

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.table = [[{"sums": None, "val": 0} for w in range(ord(W) - ord("A") + 1)] for r in range(H)]
        
    def parse(self, rows):
        c = collections.Counter()
        for item in rows:
            a, b = item.split(":")[0], item.split(":")[1] if ":" in item else item
            for colCh in range(ord(a[0]), ord(b[0]) + 1):
                for row in range(int(a[1:]), int(b[1:]) + 1):
                    c[(row, chr(colCh))] += 1
        return c

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: None
        """
        self.table[r - 1][ord(c) - ord("A")] = {"val": v, "sums": None}

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        cell = self.table[r - 1][ord(c) - ord("A")]
        if not cell["sums"]: return cell["val"]
        ret = 0
        for item, count in cell["sums"].items():
            ret += count * self.get(*item)
        return ret

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        ct = self.parse(strs)
        cell = self.table[r - 1][ord(c) - ord("A")]
        cell["sums"] = ct
        return self.get(r, c)
        