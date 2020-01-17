# Nathan Zhu, American Express, Sunday 12:16 pm, July 14th, 2019, 200 Vessey Street
# Leetcode 429 | easy | EZ
# 
# Should be able to do a n-ary level-order and any level-order in your sleep.
# So vital for any BFS.


def nary_level_order(root):
    """
    :type root: Node
    :rtype: List[List[int]]
    """
    if not root: return []
    queue, ret = [root], []
    
    while queue:
        queue_next = []
        ret.append([n.val for n in queue])
        for node in queue:
            for child in node.children:
                queue_next.append(child)
        queue = queue_next
    return ret