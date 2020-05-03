# Nathan Zhu March 23rd, 2020.  
# Leetcode n/a | n/a | easy
# Category: Fizzbuzz
#
# Return the most common character in an array, and if two characters
# have the same count, return the one with the smallest first index.



import heapq
# question 1
def MAXOCCUR(arr):
    c = collections.Counter(arr)
    # (occur, idx, actual number)
    pq = []
    seen = set()   # which ch have been seen?
    for i, ch in enumerate(arr):
        if ch in seen: continue
        seen.add(ch)
        heapq.heappush(pq, (-c[ch], i, ch))

    return heapq.heappop(pq)[2]


