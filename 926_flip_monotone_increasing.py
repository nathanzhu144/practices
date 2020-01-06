# Nathan Zhu 10:56 pm December 27th, 2019 Just got back from Napa Valley, hot air ballooning and napa valley today
# Leetcode 926 | medium | interesting idea
# Category: Sliding window

def minFlipsMonoIncr(S):
    """
    :type S: str
    :rtype: int
    """

    # A monotonically increasing array of 1s and 0s has a point where all zeroes become 1s.
    # prefix_one[i] represents how many 1s in string S[:i + 1]
    # suffix_zero[i] represents how many 0s are in string S[:i]
    #
    # The idea behind this is that assuming i is the point where the array becomes monotonically
    # increasing, the cost would be prefix[i] + suffix[i] - 1
    #
    # Why -1? Because of how I structured prefix and suffix arrays, both are inclusive of i.
    # As S[i] is a 1 or a 0, we would be overcounting a bit we have to flip.
    #
    
    suffix_zero = [0] * len(S)
    prefix_one = [0] * len(S)
    N = len(S)
    
    for i in range(N - 1, -1, -1):
        if i == N - 1:
            suffix_zero[-1] = int(S[-1] == '0')
        else:
            if S[i] == '0': suffix_zero[i] = suffix_zero[i + 1] + 1
            else: suffix_zero[i] = suffix_zero[i + 1]
        
    for i in range(0, N):
        if i == 0:
            prefix_one[0] = int(S[0] == '1')
        else:
            if S[i] == '1': prefix_one[i] = prefix_one[i - 1] + 1
            else: prefix_one[i] = prefix_one[i - 1]
            
    
    ret = float('inf')
    for i in range(N):
        ret = min(ret, prefix_one[i] + suffix_zero[i] - 1)
    return ret