


def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    # NOTE:
    # This line is to ensure that all numbers are in the stack. 
    # Otherwise, if s is just "54", we would return 0
    s = s + "+0"

    def helper(stack, i):
        number, prevsign = 0, "+"
        while i < len(s):
            if s[i].isdigit(): number = number * 10 + int(s[i])
            # Way this works is after recursive call, number should be the thing in 
            # parens, and is the RHS for an operation.
            # Ex. 3 * (4 + 3 * 2), result of (4 + 3 * 2) would be assigned to number
            # NOTE: i + 1 is to skip after i
            elif s[i] == "(":
                number, i = helper([], i + 1)
            elif not s[i].isspace():
                if prevsign == "+": stack.append(number)
                elif prevsign == "-": stack.append(-number)
                elif prevsign == "*": stack.append(stack.pop() * number)
                else: stack.append(int(stack.pop() / float(number)))
                number, prevsign = 0, s[i]

                # NOTE: We don't return sum(stack), i + 1 because 
                #       we have a i += 1 at the bottom, we would double increment for )
                # NOTE: We have to have this check AFTER the prevsign check.  Reason this 
                #       is necessary is we can return when not all numbers are in the stack
                #       If we have a state like stack = [3], number = 2, prevsign = -1, we want to
                #       return 3 - 2 == 1 and not 2.
                if s[i] == ")": return sum(stack), i


            i += 1

        return sum(stack)

    return helper([], 0)

if __name__ == "__main__":
    print(calculate("(1-(3-4))"))
    print(calculate("3*(4+2)+6"))