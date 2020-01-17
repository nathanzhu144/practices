# Nathan Zhu EHS 55 John Street August 2nd, 2019 9:54 pm
# Leetcode 394 | medium | kinda hard if you have never done this kinda question before
# Category: Calculator type of question (stack)
# This question is honestly really hard to explain.
#
# 
# Well, what's the roadblock here?
# Some of the problems are simple.
# 3[a] = 3aa
#
# But, what about nesting?
# dog4[3[a]]
# When we first see the 4, we don't know how to apply the 4x yet, so it is a 
# good idea to store it on a stack for future use.
#
# While we are at it, we should store string so far (currstring) onto a separate
# stack as well.
# 
# 
def decodestring(s):
    numstack = []
    stringstack = []
    currstring = ""
    currnum = 0

    for c in s:
        if c == "[":
            stringstack.append(currstring)
            numstack.append(currnum)
            currstring = ""
            currnum = 0
        elif c == "]":
            prevstring = stringstack.pop()
            num = numstack.pop()
            currstring = prevstring + num * currstring
        elif c.isdigit():
            currnum = currnum * 10 + int(c)
        else:
            currstring += c

    return currstring

if __name__ == "__main__":
    print(decodestring("3[a]"))

# Intuition
# b5[3[a]]
#  ^
# currstring = "b"
# currnum = 5
#--------------------
# Step 2:
# b5[3[a]]
#   ^
# We hit a "["
#
# numstack = [5]
# stringstack = ["b"]
# currstring = ""
# currnum = 0
#--------------------
# Step 3:
# b5[dog3[a]]
#       ^
#
# numstack = [5]
# stringstack = ["b"]
# currstring = "dog"
# currnum = 3
# --------------------
# Step 4:
# b5[dog3[a]]
#        ^
# We hit a "["
#
# numstack = [5, 3]
# stringstack = ["b", "dog"]
# currstring = ""
# currnum = 0
# --------------------
# Step 5:
# b5[dog3[a]]
#         ^
# numstack = [5, 3]
# stringstack = ["b", "dog"]
# currstring = "a"
# currnum = 0
# --------------------
# Step 5:
# b5[dog3[a]]
#          ^
# We hit a "]"
#
# numstack = [5]
# stringstack = ["b"]
# prevstring = "dog"
# num = 3
# currstring = "dog" + 3 * "a" == "dogaaa"
# currnum = 0
# --------------------
# Step 6:
# b5[dog3[a]]
#           ^
# We hit a "]"
#
# numstack = []
# stringstack = []
# prevstring = "b"
# num = 5
# currstring = "b" + 5 * dogaaa" == "bdogaaadogaaadogaaadogaaadogaaa"
# currnum = 0