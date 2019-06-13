
#   Nathan Zhu, 8:15 am, Amex tower, June 13th, 2019 in focus room on 36th floor
#   Been thinking about this problem for like a month now, and solved it finally.
#    NOTE: 
#          Perl uses a similar backtracking way to match, characters.  Has an exponential time
#          On the other hand, awk uses a finite state machine, and runtimes are orders of magnitude better
#
#    NOTE:
#    I originally had this as the base case, 
#        if index_string == -1 or index_pattern == -1:
#           return index_string == -1 and index_pattern == -1
#
#    This is under the premise that if the string OR pattern are empty, then if both are
#    not empty we do not have a match.  This is FALSE.
#
#    Ex. pattern = "c*"  string = ""
#
#    These do match, but my function would return false.
#
#       if a pattern is empty -> string has to be empty
#       not true string is empty -> pattern has to be empty
#
#    Which patterns fit empty strings?
#       pattern = "a*b*d*E*?*"
#
#    Length pattern must be even AND each odd index must have a *.
#

#    NOTE: Most solutions on leetcode when talking about the * talk about 3 different cases.  The one where a* counts
#          as a single a is unnecessary. It is redundant to the case where in the function you decide to use one a
#          and in the next recursive subcall you use a* counts as empty

        1. If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
        2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
        3, If p.charAt(j) == '*': 
             here are two sub conditions:
               1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
               2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
                              dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
                           or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a  (NOT NECESSARY)
                           or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty

#    


def isMatch(s, p):
    def pattern_is_empty(pattern):
        if len(pattern) % 2 != 0:
            return False
        else:
            for i in range(len(pattern)):
                if i % 2 == 1 and pattern[i] != "*":
                    return False
            return True 
        
    def helper(string, pattern, index_string, index_pattern, mem):
        key = (index_string, index_pattern)
        if key in mem:
            return mem[key]
        
        if index_string == -1 or index_pattern == -1:
            return index_string == -1 and pattern_is_empty(pattern[:index_pattern + 1])
        
        if string[index_string] != pattern[index_pattern] and pattern[index_pattern] != "." and pattern[index_pattern] != "*":
            mem[key] = False
        
        if string[index_string] == pattern[index_pattern] or pattern[index_pattern] == ".":
            mem[key] = helper(string, pattern, index_string - 1, index_pattern - 1, mem)
        
        if pattern[index_pattern] == "*":
            if string[index_string] == pattern[index_pattern - 1] or pattern[index_pattern - 1] == ".":
                mem[key] = helper(string, pattern, index_string, index_pattern - 2, mem) or \
                        helper(string, pattern, index_string - 1, index_pattern, mem)
            else:
                mem[key] = helper(string, pattern, index_string, index_pattern - 2, mem)
        
        return mem[key]
    
    return helper(s, p, len(s) - 1, len(p) - 1, {})

if __name__ == "__main__":
    print(isMatch("aa", "a*"))