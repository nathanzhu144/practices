#  Nathan Zhu 9:59 am Amex Building 36th floor, Thursday June 11th, 2019
#  Leetcode 1092 | hard | yeah I think hard
#  Category: DP
#  Runtime: Since we calculate LCS, Naive is 2^N.  DP version is M * N, M and N are lengths of strings
#  Space  : M * N
# 
#  WOOOOO, When typing up the code, I fixed two tables to LCS_table, and one comma, and passed all test cases.
#  Beautiful.
#
#  1. We build a table to find the longst common subsequence.
#   
#  Our table begins like this.  The 0s are because longest common subsequence between an 
#  empty string and a string is 0,
#  
#     * C A C B C
#   * $ 0 0 0 0 0
#   A 0 
#   B 0 
#   A 0
#   C 0
#
# 2. We fill in LCS table.
#    Let "ABAC" be str1, and "CACBC" be str2
#    
#              [Table] = 2d array
#
#             * C A C B C  index str2_len
#           * $ 0 0 0 0 0
#           A 0 0 1 1 1 1
#           B 0 0 1 1 2 2
#           A 0 0 1 1 2 2
#           C 0 1 1 1 2 3 <- backtrack from 3
#       index str1_len
#
# 3. We backtrack from bottom right of the grid.  The idea here is that we want the longest common
#    subsequence to be a subsequence of our string because you cannot get a shorter common supersequence
#    if you contain longest common subseq and add in rest of characters.
#
#    So, here's recurrence rules.
#    We start with indices str1_len and str2_len, both of which start at len(str1) and len(str2).
#    Now we can generate the shortest common supersequence from back to front.
#
#    1. if str1[str1_len - 1] == str2[str2_len - 1]: last two characters are equal.
#        This character MUST be part of supersequence.  So, we take it and decrement str1_len and str2_len by 1
# 
#    2. If str1_len or str2_len == 0.  This means that either string is empty.  shortest common supersequence is just rest
#       of the string.  
#
#    3. If last two characters are not equal, look to the square immediately to left or immediately up and check 
#       which one gives us the same length LCS as current square.  What this means is:
#
#         Suppose we are at table[3][4], where we have strings "ABA" and "CACB".
#         It is clear that LCS cannot contain both of the last letters "A" and "B", and that at least
#         one of the two MUST MAINTAIN A LCS OF SAME LENGTH AS CURRENT SQUARE.  Why? Suppose both the 
#         left and top square had one smaller than current square for LCS.  That means that A AND B 
#         are part of the LCS.  This is impossible, as the only way to decrease a LCS by 1 is if A and B are equal.
#
#         Long story short, look at the table.  We note that table[str1_len - 1][str2_len] > table[str1_len][str2_len - 1]
#                                          and               table[str1_len - 1][str2_len] == table[str1_len][str2_len]
#         This means that if we move one up, we can maintain the current LCS length, which we want to do.
# 
#         Therefore, we go from "ABA" -> "AB", and move "A" to our shortest_common_supersequence
    
#     


def shortest_common_supersequence(str1, str2):
    def LCS(str1, str2, LCS_table):
        for str1_len in range(1, len(str1) + 1):
            for str2_len in range(1, len(str2) + 1):
                if str1[str1_len - 1] == str2[str2_len - 1]:
                    LCS_table[str1_len][str2_len] = 1 + LCS_table[str1_len - 1][str2_len - 1]
                else:
                    LCS_table[str1_len][str2_len] = max(LCS_table[str1_len][str2_len - 1], LCS_table[str1_len - 1][str2_len])

    def backtrack_find_SCS(str1, str2, LCS_table):
        str1_len, str2_len = len(str1), len(str2)
        SCS_reversed = list()

        while str1_len or str2_len:
            if str1_len == 0:
                str2_len -= 1
                SCS_reversed.append(str2[str2_len])
            elif str2_len == 0:
                str1_len -= 1
                SCS_reversed.append(str1[str1_len])
            elif str1[str1_len - 1] == str2[str2_len - 1]:
                SCS_reversed.append(str1[str1_len - 1])
                str2_len -= 1
                str1_len -= 1
            elif LCS_table[str1_len - 1][str2_len] == LCS_table[str1_len][str2_len]:
                SCS_reversed.append(str1[str1_len - 1])
                str1_len -= 1
            elif LCS_table[str1_len][str2_len - 1] == LCS_table[str1_len][str2_len - 1]:
                SCS_reversed.append(str2[str2_len - 1])
                str2_len -= 1
        return "".join(SCS_reversed[::-1])

    LCS_table = [[0 for str2_i in range(len(str2) + 1)] for str1_i in range(len(str1) + 1)]
    LCS(str1, str2, LCS_table)
    return backtrack_find_SCS(str1, str2, LCS_table)




