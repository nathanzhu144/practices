# Nathan Zhu August 31st, 2019, 2:24 am
# Leetcode 418 | medium | medium
#
# Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.
# Your interview score of 3.21/10 beats 48% of all users.
# Time Spent: 1 hour 59 minutes 14 seconds
# Time Allotted: 2 hours

# Note:
# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word is greater than 0 and won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.

# This approach took too long and TLEd
def wordsTyping(sentence, rows, cols):
    """
    :type sentence: List[str]
    :type rows: int
    :type cols: int
    :rtype: int
    """
    # 1. Check to see if we can fit curr word on this line.
    #    - If we can, and we can add a space to end, we may be able to add another word on this line
    # 2. Otherwise, move to next line
    
    curridx = 0
    ret = 0
    
    while rows > 0:
        rem_width = cols
        while True:
            # We successfully fit on current word
            if len(sentence[curridx]) <= rem_width:
                rem_width -= len(sentence[curridx])
                curridx += 1
                
                # If we finished the sentence, we move ptr back to beginning of sentence,
                # Also, we fit one sentence on the screen
                if curridx == len(sentence):
                    curridx = 0
                    ret += 1
            # We did not fit on current word, try next row
            else:
                break
            
            # If we want to fit another word on, we definitely have to add a space
            rem_width -= 1
        rows -= 1
                
    return ret