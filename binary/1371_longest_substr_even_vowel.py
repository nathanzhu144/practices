# Nathan Zhu Wednesday, May 28th, 2020, 11:05 pm Stockton, CA
# Leetcode 1371 | medium | seen easier hards lol
# Category: Prefix XOR LOL
# NOT A SLIDING WINDOW QUESTION.
# Same as subarray sum eq 0, but with XOR. 

# observations:
# We only care about whether we have seen an even number of each vowel.  We don't care about the exact count
# A good way to represent this, is that for each vowel we have a bit which is 1, if we have an odd number of that num, and is 0 otherwise.
# To make sure these bits do not overlap, we can map them to different powers of 2 in a number, and then use XOR to update each of the bits.
#
# If we ever see two numbers with the same value, we know there is a net change of 0, and thus an even count of vowels in between.
# Ex. 

# "BELAATU"
# UOIEA         IDX
# 00000          -1
# 00010           1
# 00011           3
# 00010           4    Note we see 00010 again, this represents the substr "LAA"
# 00010           5    Again, we see 00010 again, "LAAT"
# 10010           6    
# 
# 
def findTheLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    table = dict()
    table[0] = -1   # This line is super important
                    # represents in beginning we have seen number 0 at pos -1
    mapping = dict(zip('aeiou', [1,2,3,4,5]))
    ret = 0
    
    curr = 0
    for i, ch in enumerate(s):
        if ch in "aeiou":
            curr ^= (1 << mapping[ch])
        if curr not in table: table[curr] = i
        else: ret = max(ret, i - table[curr])
    return ret