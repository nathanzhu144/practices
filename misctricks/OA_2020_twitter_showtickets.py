# Nathan Zhu Feb 2nd, 2020. Foundry Lofts.  
# Leetcode n/a | n/a | medium?
# Category: Misc tricks.
#
# https://stackoverflow.com/questions/43950000/hackerrank-buying-show-tickets-optimization
#
# There are n people standing in line to buy show tickets.Due to high demand, the venue sells tickets according to the following rules:

# The person at the head of the line can buy exactly one ticket and must then exit the line.
# if a person needs to purchase additional tickets,they must re-enter the end of the line and wait to be sold their next ticket(assume exit and re-entry takes zero seconds).
# Each ticket sale takes exactly one second.
# We express initial line of n people as an array, tickets = [tickets0, tickets1 ... ticketsN-1], where ticketsi denotes the number of tickets person i wishes to buy. If Jesse is standing at a position p in this line, find out how much time it would take for him to buy all tickets. Complete the waiting time function in the editor below. It has two parameters:

# An array, tickets, of n positive integers describing initial sequence of people standing in line. Each ticketsi describes number of tickets that a person waiting at initial place.
# An integer p, denoting Jesse's position in tickets.

# Sample Input 5 2 6 3 4 5 2 Sample Output 12 Sample Input 4 5 5 2 3 3 Sample Output 11
#
# 
# Insights, someone before you (position p) 


# Stupid, brute force method.
import collections
def waitingTime(tickets, p):
    # Write your code here
    q = collections.deque([])
    ret = 0

    for i in range(len(tickets)):
        if i == p: boo = True
        else: boo = False
        q.append((boo, tickets[i]))
    
    while q:
        isalex, tickets = q.popleft()
        ret += 1

        if isalex and tickets == 1: return ret
        if tickets > 1: q.append((isalex, tickets - 1))

# Efficient soln

import collections
def waitingTimeEfficient(tickets, p):
    ret = 0
    for i in range(len(tickets)):
        ret += min(tickets[i], tickets[p]) if i <= p else min(tickets[i], tickets[p] - 1)
    return ret

