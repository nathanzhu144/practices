#  Nathan Zhu, Monday 12:39 pm, Amex Tower, New York, NY
#  Leetcode problem 5 | medium difficulty | personal rating - trivial
#  This is a problem I've been working on several months, lol.  I finally decided to code it today.
#  The intuition is pretty simple actually...
# 
def longest_palindrome(s):
    starting = 0
    size = 1
    mem = [[False for row in range(len(s))] for col in range(len(s))] # maps (i, j) where i and j are inclusive to -> 
    
    # Base case 1: All 1-chars are palindromes
    for i in range(len(s)):
        mem[i][i] = True
    # Base case 2: Some 2-chars are palindromes
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            mem[i][i + 1] = True
            starting = i
            size = 2
    
    # We iterate through all strings of length 2+. 
    # If the left char == right char AND the substring between two is a palindrome
    # we have formed a new palindrome
    for end in range(2, len(s)):
        for start in range((end) - 1):
            if s[start] == s[end]:
                mem[start][end] = mem[start + 1][end - 1]
                # We save new palindrome if we find a longer one
                if mem[start][end] and end - start + 1 > size:
                    starting = start
                    size = end - start + 1
    
    return s[start: start + size]

if __name__ == "__main__":
    print(longest_palindrome("bab"))