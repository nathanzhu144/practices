# Nathan Zhu 10:11 pm July 3rd, 2019, in a dark room, 36th floor, AmeX building
# Leetcode 126 | hard | yeah hard
# Category:

# For word ladder I, we had a BFS of words.
# For word ladder II, we have a BFS of paths.  To see what each path connects to next
#                     we simply look at the last word in that path.  So, we do a BFS 
#                     just like we normally do by looking at the last element in the list.
#
# Lol, my solution is slower than 95% of all accepted python decisions.
# I was on the border of TLE before I converted the dictionary into a set.
#
import collections


def word_ladder_II(begin, end, dictionary):

    def helper(begin, end, dictionary):
            # we need a BFS queue
        dictionary = set(dictionary)
        BFS = [[begin]]

        while BFS:
            BFS_next = list()
            for path in BFS:
                # last word of path is new word
                word = path[-1]
                for i in range(len(word)):
                    for letter in list(map(chr, range(97, 123))):
                        potential_word = word[:i] + letter + word[i + 1:]
                        if potential_word in dictionary:
                            BFS_next.append(path + [potential_word])

            # What's the point of this line?
            # When we have seen a word, we can prune it.
            # Suppose another path finds this word; if it has to go
            # through a longer path to get to this word, it cannot be a shortest
            # path, so we can prune it.  However, we cannot prune a word after we
            # use it because a path of the same length could reach it.  Either or both
            # could be a shortest path then.
            for path in BFS_next:
                # we need to check if in dict cause what if two lists have same ending
                if path[-1] in dictionary: dictionary.remove(path[-1])

            ret = list(filter(lambda list_in: list_in[-1] == end, BFS_next))
            if ret: return ret

            BFS = BFS_next[:]

        # We get to this line when no valid paths.
        return list()

    return helper(begin, end, dictionary)

            # marking all last words
if __name__ == "__main__":
    print(word_ladder_II("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
