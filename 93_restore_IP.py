# Nathan Zhu Dec 22nd, 2019 4:30 am at Pepperridge Casino, Reno, NV
#                           Some security guard got mad at me bc I left my computer out when I went to restroom.
# Leetcode 93 | medium | medium
# Category: backtracking

def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    def helper(rest, currpath, num_left, ret):
        if not rest or num_left == 0:
            if not rest and num_left == 0:
                # We have a . in front, given how we construct currpath, so [1:]
                ret.append(currpath[1:])
            return
        
        # An eccentricity of IP addresses is that a block cannot start with a 0, unless 
        # that block is just 0.  Therefore, we have to make a block w only 0 if we see one.
        if rest[0] == "0":
            helper(rest[1:], currpath + ".0", num_left - 1, ret)
        else:
            for i in range(1, 4):
                # We need to have the check "i <= len(rest)" to avoid duplicates
                # Since the way python splicing works when the splice end index is greater than end of
                # string is that it just takes the whole string, we end up having multiple recursive
                # calls with the same string in some cases.
                if i <= len(rest) and int(rest[:i]) <= 255:
                    helper(rest[i:], currpath + "." + rest[:i], num_left - 1, ret)
        
    ret = list()
    helper(s, "", 4, ret)
    return ret