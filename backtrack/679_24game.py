# Nathan Zhu, July 14th, 2019, Amex building 36th floor, dark conference room. 11:03 am
# Leetcode 679 | hard | yeah, pretty damn hard
# Category: Backtracking, exhausting all possibilities
# Runtime: Really bad lol
# 
# Description:
# You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated 
# through *, /, +, -, (, ) to get the value of 24.
#
# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# Example 2:
# Input: [1, 2, 1, 2]
# Output: False

import math

def game_24(arr):
    # Here's the core logic
    def helper(arr, mem):
        # Checks whether we have gotten 24
        if len(arr) == 1: return is_close(arr[0], 24)
        
        # If we have seen this set of numbers NOT make 24, we return here.
        # With this optimization, my soln sped up more than 10x
        # We sort it cause, we only care about the set of numbers in arr,
        # If we can't make 24 with [1, 9], we also can't make 24 with [9, 1]
        key = tuple(sorted(arr))
        if key in mem: return mem[key]

        # 1. We iterate through all possible permutations.
        # 2. given a permutation, we take every consecutive pair, and do all 4 operations in compute,
        #    remove the pair, and replace with result
        #    and then recurse to see if that gives us a valid result
        for perm in permutations(arr):
            for i in range(len(perm) - 1):
                # BE CAREFUL ABOUT WHICH ARR YOU USE, Got a weird ass bug, for having this line...
                # for res in compute([arr[i], arr[i + 1]]):
                for res in compute([perm[i], perm[i + 1]]):
                    if helper(perm[:i] + [res] + perm[i + 2:], mem):
                        mem[key] = True
                        return True
                    # Since we are creating a new array with the helper call, we don't need to 
                    # explicitly backtrack here.
        mem[key] = False
        return False
    # Returns if two numbers are close
    def is_close(num1, num2):
        return abs(num1 - num2) < 0.001
    
    # Returns a list of lists of all perms in arr
    def permutations(arr):
        def helper(arr, curr_path, ret):
            if not arr: ret.append(curr_path)

            for i in range(len(arr)):
                helper(arr[:i] + arr[i + 1:], curr_path + [arr[i]], ret)
        returned = list()
        helper(arr, [], returned)
        return returned

    # [1, 2] -> [2, 1/2, -1, 3]
    # Do all four operations on arr[0] and arr[1]
    def compute(arr):
        ret = list()
        fir, sec = arr[0], arr[1]
        ret.append(fir * sec)
        if sec != 0: ret.append(fir / float(sec))
        ret.append(fir - sec)
        ret.append(fir + sec)
        return ret

    return helper(arr, dict())

if __name__ == "__main__":
    print(game_24([6, 9, 1]))
    #print(game_24([1, 2, 1, 2]))