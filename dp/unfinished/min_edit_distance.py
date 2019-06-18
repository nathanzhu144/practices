#  Nathan Zhu 9:45 pm, 55 John Street, New York, NY
#  The first time I understood how to do this problem was when I saw the soln to this problem
#  at a chinese restaurant in New York after my BoA interview
#  
#  Idea is simple.  See regex matching.

def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    def helper(word1, word2, mem):
        key = (word1, word2)
        if key in mem: return mem[key]
        
        # Base cases:
        # 1. If two words are the same, we need no operations
        # 2. If word1 is empty but word2 is not, we can to insert. We insert last char of word2
        # 3. If word2 is empty and word1 is not, we can to insert. We insert last char of word1
        if word1 == word2: return 0
        elif not word1 and word2: mem[key] = 1 + helper(word2[-1], word2, mem)
        elif not word2 and word1: mem[key] = 1 + helper(word1[-1], word1, mem)
        
        # Inductive step:
        # 1. If end of two words are the same, we don't need to additional step
        # 2. If end of two words are different, we can either add a character, delete a char or change a char
        elif word1[-1] == word2[-1]: 
            mem[key] = helper(word1[:len(word1) - 1], word2[:len(word2) - 1], mem)
        else: mem[key] = 1 + min(helper(word1 + word2[-1], word2, mem),                  \
                            helper(word1[:len(word1) - 1] + word2[-1], word2, mem),     \
                            helper(word1[:len(word1) - 1], word2, mem))                            
        return mem[key]
    
    return helper(word1, word2, {})
        