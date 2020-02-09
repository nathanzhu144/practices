# Nathan Zhu Feb 2nd, 2020 Panera Bread, saw Dara Woo today.  She wants to get dinnrer w the salesforce interns.
# Leetcode 722 | medium | annoying lol
# Category: fizzbuzz


def removeComments(self, source):
    """
    :type source: List[str]
    :rtype: List[str]
    """
    ret, buff, block_comm_open = [], '', False
    for string in source:
        i = 0
        
        while i < len(string):
            ch = string[i]
            
            if string[i:i + 2] == "/*" and not block_comm_open:
                block_comm_open = True
                i += 2
            elif string[i:i + 2] == "//" and not block_comm_open:
                break
            elif string[i:i + 2] == "*/" and block_comm_open:
                block_comm_open = False
                i += 2
            else:
                if not block_comm_open: buff += ch
                i += 1
        if buff and not block_comm_open:
            ret.append("".join(buff))
            buff = ''
    return ret