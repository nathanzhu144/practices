import collections

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.table = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.table[word].append(i)



    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1, idx2 = 0, 0
        word1_indices, word2_indices = self.table[word1], self.table[word2]
        ret = float('inf')

        while idx1 < len(word1_indices) and idx2 < len(word2_indices):
            ret = min(ret, abs(word1_indices[idx1] - word2_indices[idx2]))
            if word1_indices[idx1] < word2_indices[idx2]: idx1 += 1
            else: idx2 += 1

        return ret

            