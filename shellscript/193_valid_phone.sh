# Nathan Zhu April 31st, 2020 10:08 pm.  Finished 376 final yesterday, wooo!!
# Leetcode 193 | easy | easy??
# Category: shell scripts lol

# What does grep do? 
# Grep allows searching for text matching a regular expression.
# 
# In grep, "()?+{}" lose their special power and need to be escaped to be part of grep's language
# grep allows for searching for matching multiple patterns with -e 
# ^ matches beginning of line
# $ matches end of line
# {M} used to denote exactly M times of previous regex/occurrence
# [...] is a character class, which lets regex match one of characters in this group
# [^...] is a character class, in which this matches any character not in group
# (...) is used to group pattern/regex together

grep -e '^[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}$' -e '^([0-9]\{3\})[ ][0-9]\{3\}-[0-9]\{4\}$' file.txt
