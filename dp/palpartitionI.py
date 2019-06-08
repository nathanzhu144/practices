# Nathan Zhu 8:00 John Street, Sat June 8th, 2019, New York
# See word break problem and combination sum
#  
#  Ex. aab
# 
#      is aba
#    is [a] a palindrome? YES
#      If we use 'a'  curr -> ['a']
#         Is [b]a a palindrome?   YES
#            If we use 'a' curr -> ['a', 'b']
#                Is [a] a palindrome?    YES
#                   If we use the 'a' curr -> ['a', 'b', 'a']
#                   At this point, we have consumed whole string, so
#                   APPEND to returned list
#      If we do not use 'a' 
#         Is [ab]a a palindrome?  NO
#            Is [aba] a palindrome?   YES
#            At this point, we have consumed whole string, so
#            APPEND to returned list
#                     
# 
#  Let's talk about time complexity
# 
#  I believe the time complexity of this algorithm is 2^N where N is 
#  length of the string without DP.
# 
#  The inutition for this is worst case, with a string like "AAAAAAA"
#      We branch at every letter twice, leading to 2^N
#
#  But it can be reduced to N^2 with DP, as there are N^2 substrings in a string.
#  Intuition behind this fact is if a string is defined with a starting index i
#  and an ending index j, total number of str[i:j] must be constrained by N^2 as 
#  there are N 'i' and N 'j' possible.
#
#  Note: Word break should also have same complexity, 2^N

#  WHATS THE TIME COMPLEXITY

def partition(s):
    def ispalindrome(s):
        return s == s[::-1]
    """
    :type s: str
    :rtype: List[List[str]]
    """
    returned = [[]] #list of partitions
    def helper(s, path, returned):
        if not s:
            returned.append(path[:])
            return
        
        for i in range(len(s)):
            if ispalindrome(s[:i+1]):
                path.append(s[:i+1])
                helper(s[i+1:], path, returned)
                path.pop()

    
    helper(s, [], returned)
    return returned

if __name__ == "__main__":
    print(partition("aab"))