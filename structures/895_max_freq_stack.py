# Nathan Zhu Jan 10th, 2019 8:21 pm Foundry Lofts
# Leetcode 895 | hard | omg so elegant, so hard to think of
# Category: Design
#
# Draw it out, so beautiful.


import collections
class FreqStack(object):

    def __init__(self):
        self.c = collections.Counter()
        self.groups = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.c[x] += 1
        freq = self.c[x]
        self.max_freq = max(freq, self.max_freq)
        self.groups[freq].append(x)
        
        

    def pop(self):
        """
        :rtype: int
        """
        x = self.groups[self.max_freq].pop()
        if not self.groups[self.max_freq]: self.max_freq -= 1
        self.c[x] -= 1
        
        return x
        
