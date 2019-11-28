#  Nathan Zhu November 21st, 2019 6:33 am Duderstadt library 2nd floor.
#  Leetcode 609 | medium | EZ bro
#  Category: Easy hashtable / fizzbuzz
# 
#  "Somewhat dull and uninspiring"
#  Idea is that we are given all files in a particular folder and their contents, and we want
#  to figure out which ones have the same contents.  Hardest part is understanding the question and parsing.

import collections

def findDuplicate(paths):
    """
    :type paths: List[str]
    :rtype: List[List[str]]
    """
    ret = collections.defaultdict(list)
    for line in paths:
        data = line.split()
        root = data[0]
        for file in data[1:]:
            filename, garbage, filecont = file.partition("(")           # partition returns "before" "at" "after"
            ret[filecont[:-1]].append(root + "/" + filename)            # filecont[:-1] is because last char is always a ")"
            
    return [ret[key] for key in ret if len(ret[key]) > 1]
                