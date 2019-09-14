



def calculate(s):
    s += '+0'
    stack, num, preOp = [], 0, "+"
    for i in range(len(s)):
        if s[i].isdigit(): num = num * 10 + int(s[i])
        elif not s[i].isspace():
            if   preOp == "-":  stack.append(-num)
            elif preOp == "+":  stack.append(num)
            elif preOp == "*":  stack.append(stack.pop() * num)
            else:               stack.append(int(stack.pop() / num))
            preOp, num = s[i], 0
    return sum(stack)


print(calculate(" 3+5/2"))