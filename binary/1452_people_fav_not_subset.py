# Nathan Zhu May 16th, 2020 Stockton, CA During weekly contest, man Q4 was a killer circle sweep line question
# Leetcode 1452 | medium | medium
# Category: bitmasking
# A lot of ppl were complaining bout this one.  I thought my soln was pretty elegant.

def peopleIndexes(self, arr):
    """
    :type favoriteCompanies: List[List[str]]
    :rtype: List[int]
    """
    string_map = dict()
    person_to_bit = dict()
    ret = []

    i = 0
    for favlist in arr:
        for item in favlist:
            if item not in string_map:
                string_map[item] = i
                i += 1

    for i, fav_list in enumerate(arr):
        bits = 0
        for item in fav_list:
            bits |= (1 << string_map[item])
        person_to_bit[i] = bits


    for person, bits in person_to_bit.items():
        push = True
        for person_other, bits_other in person_to_bit.items():
            if person == person_other: continue
            if (bits & bits_other) == bits:  # person subset other
                push = False
                break
        if push: ret.append(person)

    ret.sort()
    return ret