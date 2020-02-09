# Nathan Zhu Feb 4th, 2020 8:13 pm South Quad, just ate dinner with Paul.
# Leetcode 1306 | medium | not at all bad
# Category: BFS

import collections
def canReach(arr, start):
    """
    :type arr: List[int]
    :type start: int
    :rtype: bool
    """
    q = collections.deque([start])
    visited = set()
    while q:
        curr = q.popleft()
        visited.add(curr)
        
        if arr[curr] == 0: return True
        left, right = curr - arr[curr], curr + arr[curr]
        
        if left >= 0 and left not in visited: q.append(left)
        if right < len(arr) and right not in visited: q.append(right)
        
    return False