# /* Nathan Zhu Friday July 24rd, 2020 5:34 am Stockton, CA.  Rak joined leetcode group yesterday.  Also, watching kissing booth 2 apparently.
# *  Leetcode 1311 | medium | easy
# *  Category: BFS
# */


import collections

def watchedVideosByFriends(watched, friends, myid, level):
    """
    :type watchedVideos: List[List[str]]
    :type friends: List[List[int]]
    :type id: int
    :type level: int
    :rtype: List[str]
    """
    # Doing a BFS to depth k, 
    q = collections.deque([myid])        # queue for BFS
    visited = set([myid])                # visited to avoid repeats
    while level:
        clen = len(q)
        
        for i in range(clen):
            curr = q.popleft()
            for neigh in friends[curr]:
                if neigh in visited: continue
                visited.add(neigh)
                q.append(neigh)
        level -= 1

    # Now BFS should have all neighs we care about.
    c = collections.Counter()
    while q:
        curr = q.popleft()
        for video in watched[curr]:
            c[video] += 1
            
    counts = []
    for video, count in c.items():
        counts.append((count, video))
        
    counts.sort()
    return [v for c, v in counts]
        