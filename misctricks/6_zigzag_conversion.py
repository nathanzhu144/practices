# Nathan Zhu 10:31 pm January 3rd, 2019
# Leetcode 6 | medium | this one has bothered me a year man, but it turned out to be really easy
# Category: Fizzbuzz / misc tricks

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1: return s  # EDGE CASE NEEDED
    
    ret = [[] for i in range(numRows)]
    
    dirs = 1
    curr = -1
    for i in range(len(s)):
        curr += dirs
        ret[curr].append(s[i])

        if curr + dirs == numRows or curr + dirs == -1: dirs *= -1
            
    
    return "".join("".join(arr) for arr in ret)
        
        

if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 1))