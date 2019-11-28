# Nathan Zhu Monday Nov 25th, 2019, Hatcher Ref room.
# Leetcode 1181 | medium | medium
# Non-trivial
#
# What the heck is the runtime of this thing?
# Here's what I'm thinking, the worst case for this thing is N^2, where M is the size of the list.
#
# Ex. ["aAAZa", "aBBZa", "aCCZa"]
#      We should get aAAZBBZa, aAAZCCZa, aBBZAAZa, aBBZCCZa, aCCZAAZa, aCCZBBZa,
#      which is N(N - 1), 3(3 - 1) = 6
#     
#      However, we must return all of these in sorted order.  
#      We either can generate all of thse in sorted order (possible?),
#      Or, we can generate them in any order, put them into a set, and then sort them.
#
#      I do the third option, which is KLogK, where K == N^2, so overall (N^2)Log(N^2)
# 

import collections

def beforeAndAfterPuzzles(phrases):
    """
    :type phrases: List[str]
    :rtype: List[str]
    """
    # DS 
    # front mapping "front" word of each phrase to a list of pairs (rest of phrase, idx)
    # back mapping "back" word of each phrase to a list of pairs (rest of phrase, idx)
    #
    # idx is to ensrue we don't combine same phrase with itself.
    
    front, back = collections.defaultdict(list), collections.defaultdict(list)
    for idx in range(len(phrases)):
        temp = phrases[idx].split()
        first_word = temp[0]
        first_word_map = " ".join(temp[1:])     # First word map DOESN'T include connecting word
        
        last_word = temp[-1]
        last_word_map = " ".join(temp[:])       # Last word map DOES include connecting word.
            
        front[first_word].append((first_word_map, idx))
        back[last_word].append((last_word_map, idx))
        
    
    ret = set()
    for back_word in back:
        for back_phrase, back_phrase_idx in back[back_word]:
            for front_phrase, front_phrase_idx in front[back_word]:
                # this check is to see if we combine a phrase with itself
                if back_phrase_idx != front_phrase_idx:
                    # Point if this is suppose we have ["a", "a"] -> should be "a" when combined, not "a "
                    if not front_phrase: ret.add(back_phrase)
                    else: ret.add(back_phrase + " " + front_phrase)
                    
    
    return sorted([r for r in ret])