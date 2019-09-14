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

                
def palindrome(s):
    """
    :type s: str
    :rtype: int
    """
    mem = [[False for col in range(len(s))] for row in range(len(s))]
    visited = set()

    returned = 0
    for start in range(len(s) - 1, -1, -1):
        for end in range(start, len(s)):
            mem[start][end] = ((s[start] == s[end]) and (end - start <= 1 or mem[start + 1][end - 1]))
            if s[start:end + 1] in visited: continue

            if mem[start][end]: 
                returned += 1
                visited.add(s[start:end + 1])
    return returned
    

if __name__ == "__main__":
    print(countSubstrings("aabaa"))