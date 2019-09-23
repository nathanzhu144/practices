# Nathan Zhu September 15th, 2019, 9:51 pm Johnny's house - it has been a long Sunday
# Leetcode 30 | hard | pretty hard
# 


import collections

def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if not s or not words: return []
    
    wordbag = collections.Counter(words)
    word_len = len(words[0])
    total_len = len(words) * word_len
    ret = []

    for i in range(len(s) - len(words[0]) * len(words) + 1):
        seen = collections.Counter()
        for j in range(i, i + total_len, word_len):
            curr_word = s[j : j + word_len]
            if curr_word in wordbag:
                seen[curr_word] += 1
                if seen[curr_word] > wordbag[curr_word]:
                    break
            else: break

        if seen == wordbag: ret.append(i)
    return ret


if __name__ == "__main__":
    print(findSubstring("barfoothefoobarman", ["foo", "bar"]))
