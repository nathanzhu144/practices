import collections

# class TrieNode:
#     def __init__(self):
#         self.ends = False
#         self.word = ""
#         self.table = collections.defaultdict(TrieNode)

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def add_word(self, word):
#         curr = self.root
#         for ch in word: curr = curr.table[ch]
#         curr.word = word
#         curr.ends = True

#     # is this word a subsequence of the other bigger word
#     #
#     def find_word(self, word):
#         def helper(i, node, skipped):
#             if i == len(word):
#                 if skipped: return True
#                 else: return False
#             if word[i] not in node.table or not skipped: 
#                 for ch in node.table:
#                     if i > 0: 
#                         if helper(i, node.table[ch], True): return True
#                     else: 
#                         if helper(i, node.table[ch], False): return True
#             if word[i] in node.table: return helper(i + 1, node.table[word[i]], skipped)

#         return helper(0, self.root, False)


# def findKangarooScore(words, wordsToSynonyms, wordsToAnyonyms):
#     w_to_syn, w_to_ant = collections.defaultdict(list), collections.defaultdict(list)
#     joey_to_kang = collections.defaultdict(list)
#     ret = 0

#     def nchoose2(n):
#         return (n * (n - 1)) // 2

#     for string in wordsToSynonyms:
#         string = string.lower()
#         a, b = string.split(":")
#         w_to_syn[a] = b.split(",")

#     for string in wordsToAnyonyms:
#         string = string.lower()
#         a, b = string.split(":")
#         w_to_ant[a] = b.split(",")

#     for word in words:
#         word = word.lower()
#         t = Trie()
#         t.add_word(word)
        
#         for syn in w_to_syn[word]:
#             if t.find_word(syn): 
#                 ret += 1
#                 joey_to_kang[syn].append(word)
#                 print(word, syn, "synonym found")
#         for ant in w_to_ant[word]:
#             if t.find_word(ant): 
#                 ret -= 1
#                 joey_to_kang[ant].append(word)
#                 print(word, ant, "ant found")

#     for k, v in joey_to_kang.items():
#         ret += nchoose2(len(v))
#     return ret

        
        


# if __name__ == "__main__":
#     t = Trie()
#     # t.add_word("dogger")
#     # assert(not t.find_word("do"))
#     # assert(t.find_word("oer"))
#     # assert(not t.find_word("gg"))
#     # assert(not t.find_word("r"))
#     # assert(not t.find_word("dggre"))
#     # assert(t.find_word("dgger"))
#     t.add_word("illuminated")
#     assert(t.find_word("lit"))
#     words = ["illuminated", "animosity", "deoxyribonucleic", "container", "lit", "amity", "encourage", "lighted"]
#     wordsToSynonyms = ["encourage:urge,boost,inspire", "container:tin,can,bag,bottle", "lighted:lit", "illuminated:lit"]
#     wordsToAntonyms = ["encourage:discourage", "animosity:amity,like", "lighted:dark"]

#     print(findKangarooScore(words, wordsToSynonyms, wordsToAntonyms))


def getMinGates(landingTimes, takeOffTimes, maxWaitTime, initiaPlanes):
    landing = collections.deque(landingTimes)
    takeoff = collections.deque(landingTimes)

    waiting = collections.deque()
    for i in range(0, 2360):
        if int(str(i)[-2:]) > 60: continue

        


