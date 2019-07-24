# Nathan Zhu Amex Building, 
# 
def numberToWords(self, num):
    """
    :type num: int
    :rtype: str
    """
    Less20 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve \
                Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
    Less100 = "Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
    Big1000 = "Thousand Million Billion Trillion".split()
    Less20.insert(0, "")
    Less100.insert(0, "")
    Big1000.insert(0, "")

    # assumes num < 1000
    def helper(num):
        if num == 0: return ""
        if num < 20: return Less20[num] + " "
        if num < 100: return Less100[num / 10] + " " + helper(num % 10)
        else: return Less20[num / 100] + " Hundred " + helper(num % 100)

    is_neg = False

    if num == 0: return "Zero"
    if num < 0: 
        num *= -1
        isNeg = True

    ret_word = ""
    counter = 0
    while num != 0:
        if num % 1000 != 0:
            ret_word = helper(num % 1000) + Big1000[counter] + " " + ret_word
        num = num // 1000
        counter += 1

    return ret_word.strip() if not is_neg else "-" + ret_word.strip()