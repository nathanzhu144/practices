# Nathan Zhu May 1st, 2020. Finished 376 final 3 days ago.  IT be a good time.  Watched Code-8 with Hershal & crew today
# Leetcode 420 | hard | effin hard
# Category: Misc tricks
# I'm actually really proud of this one - this one took a long time.

def strongPasswordChecker(s):
    """
    :type s: str
    :rtype: int
    """
    num_missing = 3

    if any('a' <= c <= 'z' for c in s): num_missing -= 1
    if any('A' <= c <= 'Z' for c in s): num_missing -= 1
    if any(c.isdigit() for c in s): num_missing -= 1
        
    changes = 0

    N, i = len(s), 2
    ones, twos = 0, 0   # number of changes removed by 1 del, 2 deletes

    while i < N:
        if s[i] == s[i - 1] and s[i] == s[i - 2]:
            curr = s[i]
            length = 2
            while i < N and curr == s[i]:
                length += 1
                i += 1
                
            if length % 3 == 0: ones += 1
            elif length % 3 == 1: twos += 1
            changes += length // 3
        else:
            i += 1

    if N < 6:
        return max(num_missing, 6 - N)
    elif 6 <= N <= 20:
        return max(num_missing, changes)
    else:
        # See explanation page for this logic, this took me like 4 days of thinking lol
        to_del = N - 20
        to_del_left = to_del
        
        changes -= min(to_del, ones)
        to_del_left -= ones
        
        changes -= min(max(to_del_left, 0), 2 * twos) // 2
        to_del_left -= twos * 2
        
        changes -= min(max(to_del_left, 0), 3 * changes) // 3
        
        return to_del + max(num_missing, changes)
if __name__ == "__main__":
    print(strongPasswordChecker("1AaaaBaaaaBaaaaBaaaaBaaaabcdefghijklmopqrs"))