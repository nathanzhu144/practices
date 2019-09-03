# Nathan Zhu Thursday August 22, 12:25 am. Stockton California
# Leetcode 763 | medium | medium
# Category: sliding window
# This is a typical sliding window question.
# 
# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so 
# that each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".

import collections

def partitionLabels(self, S):
    """
    :type S: str
    :rtype: List[int]
    """
    c = collections.Counter(S)
    
    # curr_set is all characters seen in current partition
    # num_finished is how many of those characers in curr_set have all their chars seen
    # last_cut is posiiton of last cut
    # ptr points to part of string we have processed so far
    #
    # ret is final returned list of partition lengths
    curr_set = set()
    num_finished = 0
    lastcut, ptr = -1, 0 # NOTE: lastcut begins at -1
    ret = list()
    while ptr < len(S):

        curr_set.add(S[ptr])
        c[S[ptr]] -= 1
        if c[S[ptr]] == 0: num_finished += 1

        if num_finished != 0 and len(curr_set) == num_finished:
            ret.append(ptr - lastcut)
            lastcut = ptr
            num_finished = 0
            curr_set = set()

        ptr += 1

    return ret