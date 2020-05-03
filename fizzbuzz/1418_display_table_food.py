
# Nathan Zhu April 19th, 2020. Stockton, CA Weekly contest 185, position 225 / 9206, a bit above top 2.5%.  First contest to get all 4 qs, also no WAs.
# Leetcode 1418 | medium | easy
# Category: fizzbuzz 
# 

import collections
def displayTable(self, orders):
    """
    :type orders: List[List[str]]
    :rtype: List[List[str]]
    """
    tables, foods = set(), set()
    food_on_table = collections.defaultdict(lambda: collections.defaultdict(int))
    
    for name, table, food in orders:
        food_on_table[table][food] += 1
        tables.add(table)
        foods.add(food)
    
    s_foods = sorted(list(foods))
    s_tables = sorted(map(int, list(tables)))
    ret = []
    ret.append(["Table"] + s_foods)
    
    for t in s_tables:
        curr = [str(t)]
        for food in s_foods:
            curr.append(food_on_table[str(t)][food])
        ret.append(map(str, curr))
        
    return ret