# Nathan Zhu January 2nd, 2019 8:01 am
# Leetcode 843 | hard | cool one
# 
# The first question is, where do the words come from?  Since these
# are randomly generated words, the probably two 6 char words have 0 in common is 
# very high:
#
# (25 / 26) ^ 6.  Most guesses will result in 0 matches.
#
# Therefore, we want to minimize the worst case of 0 matches.  We pick the word
# that has the fewest number of 0 matches with all other words.  Then, after an unsuccessful guess,
# we filter words based on which words have the same number of matches with that guess.

def findSecretWord(wordlist, master):
    """
    :type wordlist: List[Str]
    :type master: Master
    :rtype: None
    """
    def common(word1, word2):
        ret = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]: ret += 1
        return ret
    
    
    words = wordlist[:]
    
    for c in range(10):
        num_no_match = float('inf')
        
        for i in range(len(words)):
            num_zeroes = 0
            for j in range(len(words)):
                if common(words[i], words[j]) == 0: num_zeroes += 1
            if num_zeroes < num_no_match:
                next_guess = i
                num_no_match = num_zeroes
        ret = master.guess(words[next_guess])
        
        new_words = [word for word in words if common(word, words[next_guess]) == ret]
        words = new_words
    