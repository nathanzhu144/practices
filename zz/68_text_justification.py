# Nathan Zhu Tuesday Sept 10th, 2019
# Leetcode 68 | hard | pretty rough man
# Category: Greedy
#
# Yo I hate this question lol, it is one of those trash questions...
#
def full_justify(words, maxwidth):
    currline, ret = list(), list()
    num_chars_in_words = 0
    for word in words:
        # We enter this if statement if we determine we can't fit another word in this line
        if len(word) + num_chars_in_words + len(currline) > maxwidth:
            # this is where the magic happens - we allocate the spaces on current line
            # in a round robin fashion
            for i in range(maxwidth - num_chars_in_words):
                currline[i % (len(currline) - 1 or 1)] += " "
            ret.append("".join(currline))
            currline, num_chars_in_words = list(), 0
        currline += [word]
        num_chars_in_words += len(word)
    # On very last line, we want to make sure that everything is spaced by 1,
    # Also, we want to left justify by a maximum of maxWidth characters
    return ret + [" ".join(currline).ljust(maxwidth)]



    

if __name__ == "__main__":
    print(full_justify(["This", "is", "an", "example", "of", "text", "justification."], 16))