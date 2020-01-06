# Nathan Zhu Winter break December 20th, 2019 
# timed mock interview, random company
# Leetcode 797 | easy | EZ
# Category: Fizzbuzz, priority queue

# This is just a read-the-problem implement the soln kinda problem.  Using a priority queue helps.

# Given a list of scores of different students, return the 
# average score of each student's top five scores in the order of each student's id.

# Each entry items[i] has items[i][0] the student's id, and items[i][1] the 
# student's score.  The average score is calculated using integer division.
import collections
import heapq

class TopFive(object):
    def __init__(self, sid):
        self.pq = []
        self.student_id = sid
        
    def add_score(self, score):
        heapq.heappush(self.pq, score)
        
        if len(self.pq) > 5:
            heapq.heappop(self.pq)
        
    def top_five_avg(self):
        return sum(self.pq) // 5
        
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        table = dict()
        ret = list()
        max_id = -1
        
        for id, score in items:
            if id not in table: 
                table[id] = TopFive(id)
                
            table[id].add_score(score)
            max_id = max(id, max_id)
        
        for i in range(1, max_id + 1):
            ret.append([i, table[i].top_five_avg()])
        return ret