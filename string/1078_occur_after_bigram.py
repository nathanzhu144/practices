# Nathan Zhu August 27th, 2019 10:47 pm 
# Leetcode 1078 | easy | EZ
# Google- On-Site Interview
# Your interview score of 7.03/10 beats 90% of all users.
# Time Spent: 1 hour 4 minutes 24 seconds
# Time Allotted: 2 hours

# Given words first and second, consider occurrences in some text of the form "first second third", 
# where second comes immediately after first, and third comes immediately after second.
# For each such occurrence, add "third" to the answer, and return the answer.


def findOcurrences(text, first, second):
    """
    :type text: str
    :type first: str
    :type second: str
    :rtype: List[str]
    """
    textlist = text.split(" ")
    ptr = 0
    ret = list()
    
    while ptr < len(textlist) - 2:
        if textlist[ptr] == first and textlist[ptr + 1] == second:
            ret.append(textlist[ptr + 2])
            
        ptr += 1
        
    return ret