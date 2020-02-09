#   Nathan Zhu July 22nd, 2019, 11:49 am, 36th floor, Amex building
#   Leetcode 336 | hard | edge cases hard, idea kinda hard
#   Category: Can be done with trie (not done yet)
#
#   https://fizzbuzzed.com/top-interview-questions-5/
#   Time complexity of this solution is O(n * w^2) n being length of the list, 
#   w being the average word length. It is not better or worse than O(n^2), 
#   if the average word length is very long this solution is very slow, but with
#    very long list and every word is very short this is a much better solution.
#
#  There are really two big cases...
# 
def palindromePairs(words):
    def ispalindrome(word): return word == word[::-1]
    ret = []
    wordtoindex = {word: i for i, word in enumerate(words)}

    for word, k in wordtoindex.items():
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]
            # Case 1:
            # Find all words, B, shorter than or the same size as
            # word1, that can be prepended so B + word1 is a palindrome.
            #
            #         [aba] dog
            #         pfix  sffx 
            # Suppose we can find "god". Then, it is possible to form god [aba] dog
            # 
            # Why do we need wordtoindex[suffix[::-1]] != k?
            #         [aba] ""
            #         pfix sffx 
            # If we have an empty sfix, and we find "aba" elsewhere in list as a separate word, abaaba is a 
            # valid palindrome pair, but if we only have 1 unique aba in whole list, this is not possible.
            # That check checks if the pairing is valid in this case.
            #
            if ispalindrome(prefix) and suffix[::-1] in wordtoindex and wordtoindex[suffix[::-1]] != k:
                ret.append([wordtoindex[suffix[::-1]], k])
            
            # Suppose j == len(word)
            if j == len(word): continue

            # Case 2 - Find all words, B, shorter than word1 that can be appended
            # so word1 + B is a palindrome.
            #         dog [aba]
            #         pfix sffx
            # 
            # We know the suffix is a palindrome, so if we find "god", it is possible to make dog [aba] god.
            # Same reason for check.
            elif ispalindrome(suffix) and prefix[::-1] in wordtoindex and wordtoindex[prefix[::-1]] != k:
                ret.append([k, wordtoindex[prefix[::-1]]])
    return ret

if __name__ == "__main__":
    print(palindromePairs(["a",""]))