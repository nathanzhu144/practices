# Nathan Zhu May 12th, 2020, Stockton, CA, Native exotics order came today, with a free malinu basin veitchii!  Going cherrypicking tomorrow.
# Leetcode 218 | hard | damn cool
# Category: Segment tree


import collections

class SegmentTree(object):
    def __init__(self, mini = 0, maxi = 10 ** 9):
        self.seg = collections.Counter()
        self.lazy = collections.Counter()
        self.left, self.right = mini, maxi

    def update_lazy(self, start, end, id):
        if self.lazy[id] != 0:
            if start != end:
                self.seg[id * 2] = max(self.seg[id * 2], self.lazy[id])
                self.seg[id * 2 + 1] = max(self.seg[id * 2 + 1], self.lazy[id])
                self.lazy[id * 2] = max(self.lazy[id * 2], self.lazy[id])
                self.lazy[id * 2 + 1] = max(self.lazy[id * 2 + 1], self.lazy[id])
            self.lazy[id] = 0

    def add_segment(self, add_start, add_end, height):
        def helper(add_start, add_end, start, end, val, id):
            if start > end: return

            self.update_lazy(start, end, id)

            if add_start > end or add_end < start: return
            elif add_start <= start <= end <= add_end:
                self.seg[id] = max(self.seg[id], val)
                self.lazy[id] = max(self.seg[id], self.lazy[id])
            else:
                mid = (end - start) // 2 + start
                helper(add_start, add_end, start, mid, val, id * 2)
                helper(add_start, add_end, mid + 1, end, val, id * 2 + 1)
                self.seg[id] = max(self.seg[id * 2], self.seg[id * 2 + 1])

        helper(add_start, add_end, self.left, self.right, height, 1)

    def get_segment(self, get_start, get_end):
        def helper(get_start, get_end, start, end, id):
            if start > end: return float('-inf')
            self.update_lazy(start, end, id)

            if get_start > end or get_end < start: return float('-inf')
            elif get_start <= start <= end <= get_end: return self.seg[id]
            else:
                mid = (end - start) // 2 + start
                l = helper(get_start, get_end, start, mid, id * 2)
                r = helper(get_start, get_end, mid + 1, end, id * 2 + 1)
                return max(l, r)
        return helper(get_start, get_end, self.left, self.right, 1)

def getSkyline(buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    if not buildings: return []

    visited = set()
    for s, e, height in buildings:
        visited.add(s)
        visited.add(e)           # technically end is not part of the building I thinks

    visited = sorted(list(set(visited)))
    seg = SegmentTree(visited[0], visited[-1] + 1)
    for s, e, height in buildings:
        seg.add_segment(s, e - 1, height)

    last_h = 0
    ret = []
    for x in visited:
        curr_h = seg.get_segment(x, x)
        if curr_h != last_h:
            last_h = curr_h
            ret.append((x, last_h))
    return ret

if __name__ == "__main__":
    print(getSkyline([[3,7,15],[5,10,12]]))