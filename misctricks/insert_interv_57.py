def insert(self, intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    left, right = list(), list()
    new_interv_l, new_interv_r = newInterval[0], newInterval[1]
    
    for i in intervals:
        if i[1] < new_interv_l: left.append(i)
        elif i[0] > new_interv_r: right.append(i)
        else: 
            new_interv_l = min(new_interv_l, i[0])
            new_interv_r = max(new_interv_r, i[1])
            
    return left + [[new_interv_l, new_interv_r]] + right   
            
            
    
        
    # So, the question is whether inserting an interval can expand the middle interval
    # large enough to "overlap" with intervals in left or right. However, this is actually
    # impossible because the intervals originally are 
    
            # [1, 2] [3, 5] 