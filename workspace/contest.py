import collections
import heapq
import bisect
import itertools
import copy 

# Decode Numbers
# Programming challenge description:
# You are given an encoded message containing only numbers. You are also provided with the following mapping:

# A : 1
# B : 2
# C : 3
# ...
# Z : 26


# Given an encoded message, count the number of ways it can be decoded.
# Input:
# Your program should read lines from standard input. Each line contains an encoded message of numbers. You may assume that the test cases contain only numbers.
# Output:
# Print out the different number of ways it can be decoded. Note: 12 could be decoded as AB(1 2) or L(12). Hence the number of ways to decode 12 is 2.
# Test 1
# Test Input
# Download Test 1 Input
# 12
# Expected Output
# Download Test 1 Input
# 2
# Test 2
# Test Input
# Download Test 2 Input
# 123
# Expected Output
# Download Test 2 Input
# 3

def calculate(string):
    string = str(string)
    dp = dict()

    def helper(i):
        if i == len(string): return 1
        if i in dp: return dp[i]

        ret = 0
        ret += helper(i + 1)
        if i + 1 < len(string) and 10 <= int(string[i: i + 2]) <= 26:
            ret += helper(i + 2)
        
        dp[i] = ret
        return ret
    return helper(0)

if __name__ == "__main__":
    assert(calculate("123") == 3)
    assert(calculate("12") == 2)
    assert(calculate("56") == 1)
    
    

# import string

# def helper(s):
#     ret = []
#     for word in s.split():
#         if word and word[0] in string.ascii_lowercase: 
#             ret.append(word[0].upper() + word[1:])
#         else: ret.append(word)
#     return " ".join(ret)





    
    #print(solution([4, 3, 3, 4, 1, 2, 2, 3, 6, 5, 4, 5]))
    #print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    #func()
    
