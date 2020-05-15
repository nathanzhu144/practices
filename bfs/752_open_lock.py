# Nathan Zhu May 4th, 2020 Got above median by a decent amount on 376 Final!! Meera's virtual bday was yesterday
# Leetcode 969 | medium | medium
# Category: BFS
# Optimizations can be done, bidirectional bfs, maybe A*?


def openLock(deadends, target):
    """
    :type deadends: List[str]
    :type target: str
    :rtype: int
    """
    def transition(n):
        return [(n + 1) % 10, (n - 1 + 10) % 10]
    
    deadends = set(deadends)
    
    q = [[0] * 4]
    ret = 0
    
    while q:
        newq = []
        for item in q:
            curr = "".join(map(str, item))
            if curr in deadends: continue
            deadends.add(curr)
            if curr == target: return ret
            for i in range(4):
                for neigh in transition(item[i]):
                    newq.append(item[:i] + [neigh] + item[i + 1:])
        q = newq
        ret += 1
    return -1