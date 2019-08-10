# Nathan Zhu Friday August 9th, 2019, 8:49 pm, last night in new york, EHS 55 John Street
# 
# Notes in data structure

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Datastructures
        # key -> list[[timestamp0, value0], [timestamp1, value1], ...]
        self.table = collections.defaultdict(list)
    
    # So we know that the timestamps should be strictly increasing,
    # If we don't know timestamps are strictly increasing, we have to find
    # a good insertion point, but since timestamps are strictly increasing,
    # we can just append to end of list.
    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.table[key].append([timestamp, value])
        
    # We do a binary search inside the array looking for the biggest timestamp
    # less than or equal to timestamp.  Then, after we find that index, we 
    # return the value stored at that index (stored as value)
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr = self.table[key]
        
        retidx = -1
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (right - left) // 2 + left
            if arr[mid][0] == timestamp: return arr[mid][1]
            elif arr[mid][0] < timestamp: 
                retidx = mid
                left = mid + 1
            else:
                right = mid - 1
        
        if retidx == -1: return ""  # No such values are found
        return arr[retidx][1]
        