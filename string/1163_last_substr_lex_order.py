# Nathan Zhu March 19th, 2020, 10:30 pm, Did this cool one in spring break, took like 2 days.
# Leetcode 1163 | hard | HARD LOL
# Category: string

def lastSubstring(self, s):
    """
    :type s: str
    :rtype: str
        """
    if not s: return ""
    N, maxchar = len(s), max(s)
    table, starts = dict(), set()

    for i, ch in enumerate(s):
        if ch == maxchar:
            table[i] = i
            starts.add(i)

    while len(table) > 1:
        to_remove = set()
        for start, end in table.items():
            if end + 1 >= N: 
                to_remove.add(start)
            if end + 1 in starts: 
                to_remove.add(end + 1)
            table[start] += 1

        maxchar = max([s[end] for start, end in table.items() if start not in to_remove])
        new_table = dict()
        for start, end in table.items():
            if start in to_remove or s[end] != maxchar: continue
            new_table[start] = end
        table = new_table

    return s[list(table.keys())[0]:]