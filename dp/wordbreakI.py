
#  Nathan Zhu American Express Building, 
#
#  

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    
    def helper(sent, word_dict, mem):
        if not sent:
            return True
        
        if sent in mem:
            return mem[sent]

        for i in range(len(sent)):
            if sent[:i + 1] in word_dict:
                mem[sent] = helper(sent[i+ 1: ], word_dict, mem)
                if mem[sent]:
                    return True
                
        return False
    
    return helper(s, wordDict, {})