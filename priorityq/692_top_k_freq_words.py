# Nathan Zhu March 26th, 2020.  COVID-19, Foundry Lofts 12:46 pm
# Leetcode 692 | medium | not bad?
# Category: Priority-queue
import collections
class El:
    def __init__(self, ct, word):
        self.count = ct
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word
    

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        pq = []
        
        c = collections.Counter(words)
        
        for word, cnt in c.items():
            heapq.heappush(pq, (El(cnt, word), word))
            if len(pq) > k: heapq.heappop(pq)
        
        ret = []
        while pq:
            ret.append(heapq.heappop(pq))
        return [sec for first, sec in ret][::-1]