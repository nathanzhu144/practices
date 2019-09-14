def calculate(s):
    res, num, sign, stack = 0, 0, 1, []
    for ss in s:
        if ss.isdigit():
            num = 10*num + int(ss)
        elif ss in ["-", "+"]:
            res += sign*num
            num = 0
            sign = [-1, 1][ss=="+"]
        elif ss == "(":
            stack.append(res)
            stack.append(sign)
            sign, res = 1, 0
        elif ss == ")":
            res += sign*num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + num*sign

if __name__ == "__main__":
    print(calculate("1-(1-2)"))