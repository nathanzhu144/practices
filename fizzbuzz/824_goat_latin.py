# Nathan Zhu Jan 10th, 2019 10:30 am
# Leetcode 824 | easy | EZ
# Category: fizzbuzz 



def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """
    ret = []
    
    for i, word in enumerate(S.split()):
        new_word = []
        if string.lower(word[0]) in "aeiou":
            new_word.append(word)
        else:
            new_word.append(word[1:])
            new_word.append(word[0])
        new_word.append("ma")
        new_word.extend(["a"] * (i + 1))
        ret.append("".join(new_word))
        
    return " ".join(ret)