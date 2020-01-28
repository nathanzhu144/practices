#  Nathan Zhu Amex Building, New York, NY, 1:21 pm
#  Leetcode number 647 | medium | personal assessment, easy
#  
#  We count how many substrings are palindromes.  Repeat is ok.
#
#  Input: "aaa"
#  Output: 6
#  Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    mem = [[False for col in range(len(s))] for row in range(len(s))]
    returned = 0

    # Note by having start happen at n - 1, and end beginning at start,
    # we can have a very clean structure for the problem...
    for start in range(len(s) - 1, -1, -1):
        for end in range(start, len(s)):
            # we need s[start] == s[end]
            # If end - start <= 1, we check whether inner substr is a palindrome
            mem[start][end] = ((s[start] == s[end]) and (end - start <= 1 or mem[start + 1][end - 1]))
            if mem[start][end]: returned += 1
    return returned

if __name__ == "__main__":
    print(countSubstrings("FDGF"))