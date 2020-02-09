# Nathan Zhu Feb 3rd, 2020.  Got an interview with Bloomberg and Apple today.  And a call back from ServiceNow.  Not bad.
# Leetcode 451 | medium | not bad
# Category: Bucketsort
# Runtime O(N)

# There is a more obvious pq soln, which is NlogN time.

import collections
def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    c = collections.Counter(s)
    table = collections.defaultdict(list)
    
    for ch, count in c.items():
        table[count].append(ch)
        
    ret = []
    for i in range(len(s), -1, -1):
        for ch in table[i]:
            for j in range(i):
                ret.append(ch)
    return "".join(ret)