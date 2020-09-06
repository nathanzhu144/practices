# Nathan Zhu Thursday, May 28th, 2020, Stockton CA
# Leetcode 809 | medium | medium
# Category: Misc tricks
#
# If L is length of longest word in words and target and N are number of words, this is a L * N soln.

def expressiveWords(target, words):
    """
    :type S: str
    :type words: List[str]
    :rtype: int
    """
    def is_expressive(a, target):
        def get_next_len(string, i):
            ret, curri = 0, i
            while curri < len(string) and string[i] == string[curri]:
                curri += 1
                ret += 1
            return ret
        
        ia, itarget = 0, 0
        while ia < len(a) and itarget < len(target):
            next_len_a = get_next_len(a, ia)
            next_len_target = get_next_len(target, itarget)
            
            if next_len_target < next_len_a: return False
            if next_len_target < 3 and next_len_target != next_len_a: return False
            if a[ia] != target[itarget]: return False
            
            
            ia += next_len_a
            itarget += next_len_target
            
        return ia == len(a) and itarget == len(target)
    
    ret = 0
    for word in words:
        if is_expressive(word, target): ret += 1
    return ret