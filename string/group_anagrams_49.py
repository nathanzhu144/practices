#  American express tower, New York, 200 Vessey Street 36th floor, got rained on way to work.
#  Nathan Zhu
#  Leetcode 49 | medium | I think easy
#  June 25th, 2019 9:19 am
#
#  The key of each string is its sorted string. 
#  Use hash table.

def group_anagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    returned = []
    mapping = collections.defaultdict(list)
    
    for string in strs:
        mapping[str(sorted(string))].append(str(string))
    
    for val in mapping.values():
        returned.append(val)
        
    return returned
