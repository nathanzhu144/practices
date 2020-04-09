#  Nathan Zhu Sunday August 4th, 2019.  10:57 am EHS  55 John Street
#  Leetcode 332 | medium | hard
#  
#  Category: Eulerian graph, Hierholzer's algorithm
#  A Eulerian graph is a graph where each edge is visited once, and we know this is a eulerian
#  graph cause a eulerian path exists.  
# 
# 
#  Question:
#   Given a list of airline tickets represented by pairs of departure 
#   and arrival airports [from, to], reconstruct the itinerary in order. 
#   All of the tickets belong to a man who departs from JFK. Thus, 
#   the itinerary must begin with JFK
#
#  If there are multiple valid itineraries, you should return the itinerary that 
#  has the smallest lexical order when read as a single string. For example,
#  the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

import collections

def findItinerary(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    # Table maps:   airport -> [list of airports it goes to]
    # Ex. When tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    #  
    #     airport = [ 'ATL' : ['SFO', 'JFK'],
    #                 'JFK' : ['SFO', 'ATL'],
    #                 'SFO' : ['ATL'] ]
    # NOTE: Each airport maps to a lexigraphic decreasing list of airports.
    #       This is INTENTIONAL. We know that the tickets form some kind of path
    #       possibly with cycles, and we want to pick the path with a lexiographically
    #       smallest airport path.  
    #
    #       When we later try to find out path in findpath, we greedily grab the 
    #       airport at the end of the list, and pop it, ensuring we can minimize the
    #       lexigraphic size of the airplane order.
    table = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        table[a].append(b)

    
    ret = []
    def findpath(airport):
        while table[airport]:
            # Here's the greedy grabbing of lexiographically smallest.
            findpath(table[airport].pop())
        ret.append(airport)

    findpath("JFK")

    # end gets appended first .. then n - 1 ... then ... 2 ... 1
    # So, we have to reverse the whole path.
    return ret[::-1]

if __name__ == "__main__":
    print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
    print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
