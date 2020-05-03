# Nathan Zhu April 17th, 2020.  A car was smashed outside the house today, police outside.  Stockton, CA
# Leetcode 352 | hard | any uf soln is hard?
# Category: Union find / BST (done uf soln here)
# 
# Runtime: O(1) for merges, NLogN for get ranges, where N is number of distinct intervals.
#

class UF:
    def __init__(self):
        self.all_top_parents = set()            # here are all the ultimate parents
        self.parents = dict()                   # this ds tracks parent of each node
        self.parent_range = dict()              # this is the range of each parent 
        
    def find(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]
    
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb: return
        
        # in no particular order
        # make pb new ultimate parent
        # update range for pb, as it acquires range of pa
        # remove pa as an ultimate parent, as it gets merged to pb
        pa_rng, pb_rng = self.parent_range[pa], self.parent_range[pb]
        self.parent_range[pb] = [min(pa_rng[0], pb_rng[0]), max(pa_rng[1], pb_rng[1])]
        self.all_top_parents.remove(pa)
        self.parents[pa] = pb

    def add_item(self, a):
        if a in self.parents: return
        self.parents[a] = a
        self.parent_range[a] = [a, a]
        self.all_top_parents.add(a)
        
        if a + 1 in self.parents: self.union(a, a + 1)
        if a - 1 in self.parents: self.union(a, a - 1)

    def get_ranges(self):
        ret = []
        for p in self.all_top_parents:
            ret.append(self.parent_range[p])
        return sorted(ret)
        
        

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.uf = UF()
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.uf.add_item(val)
        

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.uf.get_ranges()
