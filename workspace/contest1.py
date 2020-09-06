import collections


def mostVisited(n, rounds):
    """
    :type n: int
    :type rounds: List[int]
    :rtype: List[int]
    """
    table = collections.Counter()
    
    for a, b in zip(rounds, rounds[1:]):
        i = a
        while i != b:
            table[i] += 1
            i += 1
            if i == b: break
            if i == n: i = 1
            else: 
                
    table[rounds[-1]] += 1
    ret = []
    mval = max(table.values())
    for k, v in table.items():
        if v == mval: ret.append(k)
    ret.sort()
    return ret
if __name__ == "__main__":
    print(mostVisited(2, [2,1,2,1,2,1,2,1,2]))