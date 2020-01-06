# Nathan Zhu Dec 1st, 2019 11:03 pm, Foundry Lofts, Jump Game II
# This one has haunted me for more than a year.
# Leetcode 45 | Hard | not easy to explain
# Category: BFS / greedy
# 
# Question
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

# Observations
# A super naive but intuitive approach is to do a BFS.  
# A jump would look like this.
# Position 8, max jump 4
# We can get to positions 9, 10, 11, 12
#
# This works, but we are repeating a bunch of node visits, as a node can be reached in a bunch of ways.
# Each node can represent a poin What looks like a BFS question in O(N^2) time can be improved to O(N) with an insight.
#
# The idea here is that we keep a track of a maximum distance we can get to at any point.
# 
# 
def jump_game(arr):
    if len(arr) <= 1: return 0

    currFarthest, currEnd, ret = 0, 0, 0
    for i in range(len(arr) - 1):
        currFarthest = max(currFarthest, i + arr[i])
        # This is where we move to the next set of nodes in our BFS.  
        # We jump from one of the previous nodes to the farthest node right we can get to. 
        if i == currEnd:
            ret += 1
            currEnd = currFarthest

    return ret

if __name__ == "__main__":
    print(jump_game([2,3,1,1,4]))
