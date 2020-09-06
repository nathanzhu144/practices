# Nathan Zhu, Thursday, May 28th, 2020. Stockton, CA. 7:58 pm.  
# Leetcode 722 | medium | lol kinda annoying
# Category: Parsing stuff, misc tricks


# We go through line by line.
# Keep in mind, there are three tokens of interest, "/*", "*/", "//"
# We use a boolean flag to represent whether we are in a block comment or not
def removeComments(source):
    """
    :type source: List[str]
    :rtype: List[str]
    """
    ret, curr = [], []          # ret is final return
                                # curr is buffer for holding intermediate chars
    block_com = False
    for line in source:
        i, N = 0, len(line)
        while i < N:
            if line[i:i+2] == "/*" and not block_com:
                block_com = True
                i += 2
            elif line[i:i+2] == "//" and not block_com:
                break
            elif line[i:i+2] == "*/" and block_com:
                block_com = False
                i += 2
            elif not block_com:
                curr.append(line[i])
                i += 1
            else:
                i += 1
        # This is for cases when a comment extends across multiple lines,
        # ["a/*comment", "line", "more_comment*/b"] => ["ab"] NOT ["a", "b"]
        # We only add on a new line when a block comment ends.
        if curr and not block_com: 
            ret.append("".join(curr))
            curr = []
    return ret