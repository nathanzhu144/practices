# Nathan Zhu Wednesday Sept 8th, 2019
# Not a leetcode, Citadel OA, medium (similar to friend circles)
# Category: BFS
# There are a number of animal species in the jungle.  Each species has one or more predators 
# that may be direct or indirect. Species X is a predator of Species Y
# if at least one of the following is true:

#     - Species X is a direct predator of species Y
#     - If species X is a direct predator of Z and Z is a direct predator of Y
#       then species X is an indirect predator of Y. Predation is a transitive relationship
#       that persists thru a number of levels.

# Each species has a maximum of 1 direct predator.  No two species 
# will ever be mutual predators, and no species is a predator of itself.
# Your task is to determine the minimum number of groups that must be
# formed so to ensure that no species is grouped with its predators,
# direct, or indirect.

#    0     8
#    |    / \
#    3   1   6
#    |      / \
#    5     2   9
#              |
#              7
#              |
#              4

# Groups = [0, 8]
#          [3, 1, 6]
#          [5, 2, 9]
#          [7]
#          [4]
# We need a minimum of 5 groups to satisfy all the conditions.


import heapq
import collections


def minimumGroups(predators):
    # top predators in this list
    starting = list()

    graph = collections.defaultdict(list)
    for prey in range(len(predators)):
        predator = predators[prey]

        # this prey is a top predator
        if predator == -1: 
            starting.append(prey)
            continue
        graph[predator].append(prey)

    ret = 0

    for toppredator in starting:
        Q = [toppredator]
        counter = 0
        
        while Q:
            counter += 1
            ret = max(ret, counter)
            nextQ = list()
            for predator in Q:
                # For each predator we add its prey
                if predator in graph:
                    for prey in graph[predator]:
                        nextQ.append(prey)
            
            Q = nextQ

    return ret
