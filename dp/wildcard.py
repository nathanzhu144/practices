# Nathan Zhu, 55 John Street June 17th, 2019
# Monday 8:47 pm
#
# This is a leetcode hard, but IMO it isn't that hard.
# First submit passed most test cases.  Had a slight issue with the base cases.
#
# 
#  Intuition:
#     Starting from last character of pattern & string, we want to see if the
#     last character of pattern can match last character of string
#
#     P[i][j] = P[i - 1][j - 1] && (s[i - 1] == p[j - 1] || p[j - 1] == '?'), if p[j - 1] != '*';
#     P[i][j] = P[i][j - 1] || P[i - 1][j], if p[j - 1] == '*'.
#
#     If confused, see regex matching DP question

def is_match(string, pattern):
    def pattern_can_be_empty(pattern):
        for i in pattern:
            if i != "*": return False
        return True
    
    def helper(string, pattern, string_i, pattern_i, mem):
        key = (string_i, pattern_i)
        if key in mem: return mem[key]
        
        # 1. if string is empty, see is pattern matches with empty
        # 2. if pattern is empty, see if string is empty
        if not string[:string_i + 1]: return pattern_can_be_empty(pattern[:pattern_i + 1])
        if not pattern[:pattern_i + 1]: return not string[:string_i + 1]
        
        # if ends of both pattern & string are different and pattern's end is not a spec character, we return false
        if pattern[pattern_i] != "?" and pattern[pattern_i] != "*" and pattern[pattern_i] != string[string_i]: return False
        
        # If ends of pattern and string are same or end of pattern is ?, we recur to smaller subproblem
        if pattern[pattern_i] == string[string_i] or pattern[pattern_i] == "?":
            mem[key] = helper(string, pattern, string_i - 1, pattern_i - 1, mem)

        # If pattern is "*", we can choose to use it or choose not to use it
        if pattern[pattern_i] == "*":
            mem[key] = helper(string, pattern, string_i - 1, pattern_i, mem) or helper(string, pattern, string_i, pattern_i - 1, mem)
        return mem[key]
    return helper(string, pattern, len(string) - 1, len(pattern) - 1, {})

if __name__ == "__main__":
    print(is_match("aa", "*"))