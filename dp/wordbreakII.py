

#  Nathan Zhu, American Express Tower, 6:32 am, Monday June 10th, 2019
#  
#  Given 
# 

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    
    ## This is whole recursive function
    def helper(sent, word_dict, returned, curr_path):
        if not sent:
            returned.append(curr_path)
            
        for i in range(len(sent)):
            if sent[:i + 1] in word_dict:
                helper(sent[i + 1: ], word_dict, returned, curr_path + [sent[:i + 1]])
                
    temp = []
    returned = []
    
    helper(s, wordDict, temp, [])
    
    # this converts all 
    for i in temp:
        returned.append(" ".join(i))
        
    return returned