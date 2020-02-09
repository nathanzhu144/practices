# Nathan Zhu September 11th, 2019 12:57 pm, Duderstadt library 1 day before microsoft interview
# Leetcode 283 | easy | not-so-easy if not seen insight
# 
# Given an array nums, write a function to move all 0's to the end of it while 
# maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]


def move_zeroes(arr):
    zero = 0 # Zero should track location of last 0
    for i in range(len(arr)):
        if arr[i] != 0:
            # arr[i] if enters this if statement points to first ele without a zero
            arr[zero], arr[i] = arr[i], arr[zero]
            zero += 1

    