# Nathan Zhu, Wednesday July 31st, 9:45 am.  EHS 55 John Street
# Leetcode 31 | medium | medium
# 
# This explanation expects you to know how to generate permutations recursively
# https://www.youtube.com/watch?v=quAS1iydq7U
# Let's take the permutation [6, -2, 3, 7, 6, 5, 4, 1, 1, 0]
#                                    ^  ^        ^ swaprightidx
#                                      reverseidx
#                                  swapleftidx
# 
# The idea is this: There is a decreasing section of the permutation. This decreasing
#                   section is "out of arrangements", as we only get to a decreasing orientation
#                   at a final permutation.
#
#                   Therefore, recursively our "possibilities" array looks like this
#                   
#                                [0, 1, 1, 4, 5, 6, 7]
#                                                   ^ we chose 7 as starting perm, and 
#                                                     are back onto this stack frame after
#                                                     generating all the possibilities, we are done.
#                   Therefore, we have to incorporate the previous index into the back of 
#                              our longer permutation.  How do we incorporate [3]?
#  
#                              Well, in the previous stack frame, our loop looks like this
#                              [0, 1, 1, 3, 4, 5, 6, 7]
#                                        ^ 
#                                        current
#                              As we have exhausted the possibilities for placing 3 first,
#                              we increment our loop counter,
#                              [0, 1, 1, 3, 4, 5, 6, 7]
#                                           ^ 
#                                           current
#                              so we can place 4 first instead. 
# 
#                   Next permutation is [6, -2] + [4] + [0, 1, 1, 3, 5, 6, 7]
#                              After swapping the swapleftidx and swaprightidx, 
#                              reverse everything from reverseidx to end.
#  
# These notes are pretty unclear.  I recommend keeping this idea in mind while drawing
# out an example permutation.


# Given a perm, returns next perm
def return_next_perm(arr):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # swapleftidx can be initted to anything
    reverseidx = len(arr) - 1; swapleftidx = -1; swaprightidx = len(arr) - 1
    
    # finding reverseidx
    while reverseidx > 0:
        if arr[reverseidx] > arr[reverseidx - 1]: break
        reverseidx -= 1
    # in case all are ascending
    if reverseidx == 0: return arr[::-1]
    swapleftidx = reverseidx - 1
    
    #finding swaprightidx
    while swaprightidx >= reverseidx:
        if arr[swaprightidx] > arr[swapleftidx]: break
        swaprightidx -= 1
    
    arr[swapleftidx], arr[swaprightidx] = arr[swaprightidx], arr[swapleftidx]
    return arr[:reverseidx] + arr[reverseidx:][::-1]

# Given a perm array, transforms that perm array to next perm
def reverse_in_place()
    # Reverses from index i to end of array.
    def reversetoend(arr, i):
        left, right = i, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # swapleftidx can be initted to anything
    reverseidx = len(arr) - 1; swapleftidx = -1; swaprightidx = len(arr) - 1
    
    # finding reverseidx
    while reverseidx > 0:
        if arr[reverseidx] > arr[reverseidx - 1]: break
        reverseidx -= 1
        
    if reverseidx == 0:
        reversetoend(arr, 0)
        return arr[::-1]
    
    swapleftidx = reverseidx - 1
    
    while swaprightidx >= reverseidx:
        if arr[swaprightidx] > arr[swapleftidx]: break
        swaprightidx -= 1
    
    arr[swapleftidx], arr[swaprightidx] = arr[swaprightidx], arr[swapleftidx]
    reversetoend(arr, reverseidx)
    
if __name__ == "__main__":
    print(nextPermutation([1, 3, 2]))