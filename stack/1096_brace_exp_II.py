# Nathan Zhu March 18th, 2020, Foundry Lofts 8th floor. Went outside today, been quarantined for too long.
# Leetcode 1096 | hard | pretty hard imo
# Category: Stack
# Similar questions are the calculator I and II and III questions.
#
# Use stack for "{" and "}" just like in calculator.
# Maintain two lists:

# the previous list before ",",
# the current list that is still growing.
# When seeing an "alphabet", grow the second list by corss multiplying. So that [a]*b will become "ab", [a,c]*b will become ["ab", "cb"]
# When seeing ",", that means the second list can't grow anymore. combine it with the first list and clear the second list.
# When seeing "{", push the two lists into stack,
# When seeing "}", pop the previous two lists, cross multiplying the result inside "{ }" into the second list.

# If not considering the final sorting before return, the time complexity should be O(n)
#
#
# Intuition: Think of which group is "binding", as in will be applied to current group
#            Drawing a simple state diagram when things move from "binding" to "nonbinding" and
#            back is useful for this one.

import itertools


def braceExpansionII(self, expression):
    """
    :type expression: str
    :rtype: List[str]
    """
    stack, nonbinding, binding = [], [], []

    for i, ch in enumerate(expression):
        if ch.isalpha():
            binding = [exp + ch for exp in binding or [""]]
        elif ch == "{":
            stack.append(nonbinding)
            stack.append(binding)
            binding, nonbinding = list(), list()
        elif ch == "}":
            left = stack.pop()
            preleft = stack.pop()

            right = binding + nonbinding

            binding = [l + r for r in right for l in left or [""]]
            nonbinding = preleft
        elif ch == ",":
            # Note that , makes a binding expression nonbinding, so
            # we add the binding part to the nonbinding part.
            nonbinding += binding
            binding = list()

    return sorted(set(binding + nonbinding))

if __name__ == "__main__":
    print(braceExpansionII("{{a,z},a{b,c},{ab,z}}"))
    print(braceExpansionII("{ff,gg}{ab,zf}{b,c}ef{d,f},{l,m}"))