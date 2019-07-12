

#  Nathan Zhu, American Express Tower, 6:32 am, Monday June 10th, 2019
#  Nathan Zhu (finished)  Wednesday July 3rd, 10:02 pm
#  
#  Word break's complexity is pretty bad, and what the question wants us to do is return
#  all possible word breaks of a sentence.
#
#  We can cache what each sentence breaks up into, so if we see that sentence again,
#  we can "remember" it.
#
#  I was 70% on the right track with this question, it is a hard question...
#

def word_break_II(sent, dictionary):
    def helper(sent, word_dict, visited):
        # If we have seen this sentence, return its word-broken equivalent.
        if sent in visited: return visited[sent]

        # NOTE: RETURNING AN EMPTY LIST WILL BE A BUGGER
        #       We need to return a list with an empty list inside
        #       so, when we iterate over result later, we can concatenate to it
        #       Idea is recursively that an empty sentence can be word-broken in one way
        if not sent: return [[]]
        
        # we have not seen this sentence, so we attempt to word-break it
        ret = list()
        for i in range(1, len(sent) + 1):
            if sent[:i] in word_dict:
                # Result is broken-up sent[i:].  Note that if it cannot be broken up, we return
                # an empty list.  If an empty list is returned, we won't concatenate anything to it
                # cause we will jump over it
                result = helper(sent[i:], word_dict, visited)
                for res in result:
                    ret.append([sent[:i]] + res)

        visited[sent] = ret  # we cache what sent is broken up into.
                             # even if ret is empty, that is INTENDED, as we cannot break this sentence
        return ret

    returned = helper(sent, dictionary, dict())
    return [" ".join(lis) for lis in returned]


if __name__ == "__main__":
    print(word_break_II("catsanddog", ["cat","cats","and","sand","dog"]))