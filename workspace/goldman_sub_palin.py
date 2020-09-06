

def palindrome(s):

    dp = dict()   # dp (i, j)
    hashes = dict()
    N = len(s)

    for r in range(N):
        hashi = 0
        for c in range(N):
            hashi = hashi * 26 + ord(s[c]) - ord('a')
            hashes[(r, c)] = hashi

    for i in range(N):
        dp[(i, i)] = True
    
    for i in range(N - 1):
        if s[i] == s[i + 1]: dp[(i, i + 1)] = True
        else: dp[(i, i + 1)] = False

    for end in range(2, N):
        for start in range(end - 2):
            if dp[(start + 1, end - 1)] == True and s[start] == s[end]: 
                dp[(start, end)] = True
            else: 
                dp[(start, end)] = False
            

    
            


    