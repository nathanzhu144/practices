# Nathan Zhu April 11th, 2020. Stockton,  CA.  COVID-19
# Leetcode 1410 | medium | not bad?
# Category: Fizzbuzz
# 

def entityParser(text):
    """
    :type text: str
    :rtype: str
    """
    table = dict()
    table["&quot;"] = "\""
    table["&apos;"] = "'"
    table["&amp;"] = "&"
    table["&gt;"] = ">"
    table["&lt;"] = "<"
    table["&frasl;"] = "/"

    ret = text
    for key, val in table.items():
        arr = ret.split(key)
        ret = val.join(arr)
    return ret