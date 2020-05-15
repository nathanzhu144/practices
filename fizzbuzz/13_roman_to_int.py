# Nathan Zhu April 4th, 2020, COVID-19, just finished 376 final.
# Leetcode 13 | easy | easy
# Category: fizzbuzz

def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    symbols = {"I": 1,
                "IV": 4,
                "V": 5, 
                "IX": 9,
                "X": 10,
                "XL": 40,
                "L": 50,
                "XC": 90,
                "C": 100,
                "CD": 400,
                "D": 500,
                "CM": 900,
                "M": 1000,}
    
    returned = 0
    i = 0
    
    while i < len(s):
        if i + 1 < len(s):
            if s[i: i + 2] in symbols:
                returned += symbols[s[i: i + 2]]
                i += 2
                continue
        returned += symbols[s[i]]
        i += 1
        
        return returned
