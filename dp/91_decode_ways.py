## 9:04 pm, New York, John Street, in total darkness, June 11th, 2019.
#  Leetcode 91 | med | med
#  Category: DP  
#  Did a set of 4 x 3 x 124 for overhead press today this afternoon during lunch break.
#  I was wearing a dress shirt while pressing, and some guy tapped me and told me - "That's dedication"
#  Hope I can press more next time I read this.  
#  Update: This is me on July 15th, 2019.  I think I can press less cause still cutting.
#
#  I first coded this in C++, but it kept overflowing.  Also, none of the leetcode solns are top-down.  All of them
#  are bottom-up.
#
#  NOTE: The first thing that I was afraid was double-counting strings.  I was thinking - what if 
#        I recurse by taking the first 2 chars off OR first char off, but I get the same string later on
#        down the line.  This is impossible, as if you are removing the first two chars off OR the first 
#        char off, the first letter will always be different.
#
#  NOTE: For base cases, I didn't quite understand why I returned 1 only when I hit an empty string.
#        The idea is that when I hit an empty string, I have reached a unique valid path.
#
#  NOTE: Suppose than there are two zeros in middle of a test case like "1001".  There are no ways to decode.
#        My functions get around this, as the default returned is 0, and IF there are valid ways to get to
#        N - 2 and N - 1 do I add those possibilities.
#
#  NOTE: This is very similar to an advanced Fibonacci question.  Like a Fib or stair step with more edge cases.
#
#  I implemented bottom up as well as top down approaches.
#
#  IMPORTANT: Leetcode isn't too clear on edge cases for this.  For example, is "02" -> B?  I Think the answer
#             to this is no. What do you do if you have a case like "00" in the middle of the string? 
#             Well, number of decodings should be 0, as it is not possible to decode two 0s.
#

###########################
## Python bottom up version
#
#  Faster than 38% of solutions, memory usage less than 42% of python solutions.
#
#  Key recurrence relation is kinda like Fibonacci or stair-stepping.  
#  Number of decodings of a length N string, assuming last two chars and last
#  char are decodable is simply 
#
#  Num(N) = Num(N - 2) + Num(N - 1)
#
#  This took an embarassingly long time to figure out.

def num_decodings(string):
    if not string:
        return 1

    visited = {}    # Maps length of string -> number of possible strings
    visited[0] = 1  # add 1 if you get to an empty string, as you've generated a new valid seq

    if string[0] == "0":   # If string is "0" there are no ways to decode
        visited[1] = 0
    else:
        visited[1] = 1

    
    for i in range(2, len(string) + 1):
        visited[i] = 0
        if len(string) >= 2 and int(string[i - 2:i]) <= 26 and int(string[i - 2:i ]) >= 10: # NOT int(string[i - 2:i ]) >= 0 
            visited[i] += visited[i - 2]                                                    # excludes possibilities like "02" -> "B"
        if len(string) >= 1 and int(string[i - 1: i]) <= 9 and int(string[i - 1: i]) >= 1:
            visited[i] += visited[i - 1]

    return visited[len(string)]


###########################
## Python top-down version
## Faster than 19.67% of python submissions 
#  Memory usage less than 5% of python submissions
#  Top down uses less memory, but runtime is worse I think
#
# 
def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """
    def helper(string, visited):
        if string in visited:
            return visited[string]
        
        returned = 0
        
        if len(string) == 0:
            return 1
        
        if len(string) == 1:
            if string == "0":
                return 0
            else:
                return 1
        
        if len(string) >= 2:
            if int(string[:2]) <= 26 and int(string[:2]) >= 10:
                returned += helper(string[2:], visited)
            
        if len(string) >= 1:
            if int(string[:1]) <= 9 and int(string[:1]) >= 1 and string[:1] != "0":
                returned += helper(string[1:], visited)
            
        visited[string] = returned
        
        return returned
    
    return helper(s, {})




##  C++ Top down DP solution, the python equivalent works on Leetcode, but the C++
#   version seems to have an integer overflow on test case 200/250 or so.  I tried changing
#   the int to a long long, but it didn't work.  The python version works, and I think the code is correct
#
#
#  

# int helper(string num, unordered_map<string, int>& visited){
#     int returned = 0;
    
#     if(visited.count(num)){
#         return visited[num];
#     }
    
#     if(num.size() == 0){
#         return 1;
#     }
    
    
#     if(num.size() == 1){
#         return num != "0";
#     }
    
#     if(num.size() >= 2){
#         string front = string(num, 0, 2);
#         if(stoi(front) >= 10 && stoi(front) <= 26){
#             returned += std::max(returned, helper(string(num, 2, string::npos), visited));
#         }
#     }
    
#     if(num.size() >= 1){
#         string front = string(num, 0, 1);
#         if(stoi(front) >= 1 && stoi(front) <= 9){
#             returned += std::max(returned, helper(string(num, 1, string::npos), visited));
#         }
#     }
    
#     visited[num] = returned;
#     return returned;
# }

# int numDecodings(string s) {
#     unordered_map<string, int> visited;
    
#     return helper(s, visited);
# }



    