# Nathan Zhu Thursday May 21st, 2020, 11:52 pm. Stockton, CA, COVID-19
# Leetcode 1061 | medium | medium
# Category: UF

class UF(object):
    def __init__(self):
        self.parent = dict()
        self.smallest = dict()
        
    def touch(self, a):
        if a in self.parent: return
        self.parent[a] = a
        self.smallest[a] = a
        
    def find(self, a):
        if self.parent[a] != a: self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def join(self, a, b):
        p1, p2 = self.find(a), self.find(b)
        if p1 == p2: return
            
        self.parent[p1] = p2
        self.smallest[p2] = min(self.smallest[p1], self.smallest[p2])
        del self.smallest[p1]
        
    def get_small_char(self, ch):
        if ch not in self.parent: return ch
        return self.smallest[self.find(ch)]


def smallestEquivalentString(A, B, S):
    """
    :type A: str
    :type B: str
    :type S: str
    :rtype: str
    """
    u = UF()
    for a, b in zip(A, B):
        u.touch(a)
        u.touch(b)
        u.join(a, b)
        
    return "".join([u.get_small_char(ch) for ch in S])