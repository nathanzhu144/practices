# Nathan Zhu 8/8/2019 Amex, Last few days.
# Leetcode 935 | medium | med
# Category: DP
#
# Hershal trolled me with this question for so long - it isn't even that hard


def knightDialer(N):
    """
    :type N: int
    :rtype: int
    """
    
    adjacent = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
    graph = dict()
    for i in range(len(adjacent)):
        graph[i] = adjacent[i]
        
    def helper(curr_pos, num_hops, graph, table):
        key = (curr_pos, num_hops)
        if key in table: return table[key]
        
        if num_hops == 1: return 1
        
        num_form_by_rest_digits = 0
        for node in graph[curr_pos]:
            num_form_by_rest_digits += helper(node, num_hops - 1, graph, table)
        
        table[key] = num_form_by_rest_digits % (10 ** 9 + 7)
        return table[key]
    
    
    ret = 0
    for i in range(10): ret += helper(i, N, graph, dict())
    return ret % (10 ** 9 + 7)
        