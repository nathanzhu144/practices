# Nathan Zhu Jan 31st, 2020 8:00 pm ET aboutta go to bdubs with Hershal, we going to talk about his relationship problems!
# Leetcode 1055 | medium | medium
# Category: binary search / string
# SIMILAR PROBLEMS: 392 is subseq, 792 num matching subseq

import collections
import bisect

def shortestWay(source, target):
    # find smallest larger or eq target
    def find(arr, target):
        ret = len(arr)
        left, right = 0, ret - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if arr[mid] >= target:
                ret = mid
                right = mid - 1
            else:
                left = mid + 1
        return ret
                
    table = collections.defaultdict(list)
    
    for i, ch in enumerate(source):
        table[ch].append(i)
        
    ret = 1
    i = 0
    for ch in target:
        if ch not in table: return -1
        
        newidx = find(table[ch], i)
        if newidx == len(table[ch]):
            ret += 1
            i = table[ch][0] + 1
        else:
            i = table[ch][newidx] + 1
            
    return ret
        

if __name__ == "__main__":
    print(shortestWay("abc", "abcbc"))