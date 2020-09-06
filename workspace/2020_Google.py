import collections


def solution(T):

    def is_valid(time):
        hr, mi = time.split(":")
        return 0 <= int(hr) <= 23 and 0 <= int(mi) <= 59

    rep_i = set(i for i in range(len(T)) if T[i] == '?')

    for rep in range(9, -1, -1):
        newstr = "".join(T[i] if i not in rep_i else str(rep) for i in range(len(T)))
        if is_valid(newstr):
            return newstr

    return ""
        
if __name__ == "__main__":
    assert(solution("2?:?8") == "23:38")
    assert(solution("1?:?2") == "15:52")
    assert(solution("??:??") == "22:22")
    assert(solution("06:32") == "06:32")


