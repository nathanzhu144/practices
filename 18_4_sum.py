# Nathan Zhu Dec 25th, 2019 Christmas day, 11:46 am, Stockton Californiam they are making dumplings, I am doing leetcode.
# Leetcode 18 | medium | medium/hard
# Lots of things to keep track of to make this correct.

def fourSum(arr, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    first, sec = 0, 1
    ret = list()
    N = len(arr)
    
    arr.sort()
    
    for first in range(N - 3):
        # Necessary for no redundant firsts
        if first != 0 and arr[first] == arr[first - 1]: continue
            
        for sec in range(first + 1, N - 2):
            # Necessary for no redundant seconds
            # This line is tricky af
            # sec != 0 and arr[sec] == arr[sec - 1] leads to the bug where
            # [[0, 0, 0, 0]] is not considered, as sec immediately increments
            # The idea is we check iff it isn't the first iteratin.
            if sec != first + 1 and arr[sec] == arr[sec - 1]: continue
            
            # Rest is basic 3-sum
            third, fourth = sec + 1, N - 1
            while third < fourth:
                total =  arr[first] + arr[sec] + arr[third] + arr[fourth] 
                
                if arr[first] + arr[sec] + arr[third] + arr[fourth] == target:
                    ret.append([arr[first], arr[sec], arr[third], arr[fourth]])
                
                    while third < fourth and arr[third] == arr[third + 1]: third += 1
                    while third < fourth and arr[fourth] == arr[fourth - 1]: fourth -= 1
                    third += 1
                    fourth -= 1
                    
                elif total < target:
                    third += 1
                else:
                    fourth -= 1
            
    return ret