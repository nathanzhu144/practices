# Nathan Zhu April 28th, 2020  376 exam in a few days, Stockton, California  Wekly contest 181
# Leetcode 1423 | medium | damn cool
# Category: Sliding window. 
# This is the question yash got for google.


def maxScore(arr, k):  
    N = len(arr)
    
    subarr_len = N - k
    
    min_so_fr = float('inf')
    
    left, right = 0, 0
    curr = 0
    while right < N:
        curr += arr[right]
        right += 1
        if right - left > subarr_len:
            curr -= arr[left]
            left += 1
        
        if right - left == subarr_len:
            min_so_fr = min(curr, min_so_fr)
    
    #print(min_so_fr)
    return sum(arr) - min_so_fr
        