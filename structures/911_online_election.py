# Nathan Zhu August 30, 2019 1:06 PM
# Leetcode 911 | medium | medium
# 
# Category: binary search/system design
#
# Apple- Phone Interview
# Your interview score of 3.94/10 beats 34% of all users.
# Time Spent: 1 hour 13 minutes 2 seconds
# Time Allotted: 1 hour 30 minutes


# In an election, the i-th vote was cast for persons[i] at time times[i].
# Now, we would like to implement the following query function: TopVotedCandidate.q(int t) 
# will return the number of the person that was leading the election at time t.  
# Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.


import heapq


class TopVotedCandidate(object):
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        # time_to_winner is a list of pairs [time, winner], if a time is not found,
        # winner is time immediately below
        self.time_to_winner = []
        most_recent_vote = 0
        
        max_cand_num = 0
        for i in range(len(persons)):
            if persons[i] > max_cand_num: max_cand_num = persons[i]
                
        
        candvote = [0] * (max_cand_num + 1)
        last_winner, last_max = -1, 0
        for i in range(len(persons)):
            candvote[persons[i]] += 1
            
            if candvote[persons[i]] >= last_max:
                if persons[i] != last_winner:
                    self.time_to_winner.append([times[i], persons[i]])
                last_winner = persons[i]
                last_max = candvote[persons[i]]
                
            
        
    # Does binary search for smaller or equal.
    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        left, right = 0, len(self.time_to_winner) - 1
        ret = -1
        while left <= right:
            mid = (right - left) // 2 + left
            
            if self.time_to_winner[mid][0] == t: return self.time_to_winner[mid][1]
            if self.time_to_winner[mid][0] <= t:
                ret = mid
                left = mid + 1
            else:
                right = mid - 1
        return self.time_to_winner[ret][1]
            
            
        