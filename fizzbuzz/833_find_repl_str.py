
# Nathan Zhu January 26th, 2019 9:30 pm Foundry Loft 
# Leetcode 833 | med | not too bad
# Category: Fizzbuzz
# 
# I was overthinking it with rabin karp, but I'm not sure this is too possible.
# 

def findReplaceString(S, indexes, sources, targets):
    """
    :type S: str
    :type indexes: List[int]s
    :type sources: List[str]
    :type targets: List[str]
    :rtype: str
    """
    mod = list(S)
    
    for i, src, t in zip(indexes, sources, targets):
        if not S[i:].startswith(src): continue
        else:
            mod[i] = t
            for j in range(i + 1, i + len(src)): mod[j] = ""  # used for overwriting 
                
    return "".join(mod)

if __name__ == "__main__":
    print(findReplaceString("abcd", [0,2], ["a","cd"], ["eee","ffff"]))