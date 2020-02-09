# Nathan Zhu Jan 31s, 2020 Friday at the Duderstadt, quiet day.  Julie saw a Turkey.
# Leetcode 392 | easy | tbh at least medium
# Category: binary search / string
# SIMILAR PROBLEMS: 792 num matching subseq, 1055 shortest way form string

from collections import defaultdict
from bisect import bisect_left
import collections


def isSubsequence(s, t):
    # Find idx of smallest thing greater than or equal to x.     
    # What if nothing is smaller than x, return len of arr.
    def find_smallest_greater_eq(arr, n):
        ret = len(arr)
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (right - left) // 2 + left
            if arr[mid] >= n:
                ret = mid
                right = mid - 1
            else: left = mid + 1
        print(ret)
        return ret
        
    table = collections.defaultdict(list)
    for i, ch in enumerate(t):
        table[ch].append(i)
    
    curridx = 0
    for ch in s:
        if ch not in table: return False
        
        next_char_idx = find_smallest_greater_eq(table[ch], curridx)
        if next_char_idx == len(table[ch]): return False
        curridx = table[ch][next_char_idx] + 1
    return True

