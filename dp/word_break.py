

# index is last char we are looking at
# Ex. dogbat
#          ^ index
def helper(sentence, index, dict, mem):
    if index in mem:
        return mem[index]

    if index == -1:
        return True

    for i in range(index, -1):
        if dict[i:index + 1] in dict:
            mem[index] = helper(sentence, i, dict, mem)
            return mem[index]

    mem[index] = False
    return mem[index]
        
def wordbreak(sentence, dict):
    return helper(sentence, len(sentence) - 1, dict, {})

if __name__ == "__main__":
    dictionary = {"dog", "yop"}

    print(wordbreak("dogyop", dictionary))
    print(wordbreak("yopdog", dictionary))
    print(wordbreak("yopdogd", dictionary))



