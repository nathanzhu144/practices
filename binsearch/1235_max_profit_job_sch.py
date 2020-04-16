# Nathan Zhu April 14th, 2020.  8:49 pm Stockton, CA, Covid-19
# Leetcode 1235 | hard | medium/hard
# Category: DP / binary search
# 
# Damn this smart

import bisect
def jobScheduling(startTime, endTime, profit):
    """
    :type startTime: List[int]
    :type endTime: List[int]
    :type profit: List[int]
    :rtype: int
    """
    # (starttime, endtime, profit)
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
    
    table = [[0, 0]]
    for start, end, profit in jobs:
        idx = bisect.bisect(table, [start + 1, ]) - 1  # Since there could be multiple job w same start time
                                                        # we need to get the last job w that start time, because that would show the 
                                                        # largest profit endeding at that start time
        if table[idx][1] + profit > table[-1][1]:
            table.append([end, table[idx][1] + profit])
        
    return table[-1][1]