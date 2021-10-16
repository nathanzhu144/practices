import collections

# subtracts two times, finds diff
def subtract_times(first, sec):
    buckets = []
    for a, b in zip(first.split(":"), sec.split(":")):
        a, b = float(a), float(b)

        time = b - a
        if b - a < 0:
            time += 100 if (len(buckets) == 2) else 60
            buckets[-1] -= 1
        
        buckets.append(time)

    ret = []

    for num in buckets:
        ins = str(int(num)) if len(ret) < 2 else str(num)[:4]
        while len(ins) < 2:
            ins = '0' + ins
        if len(ret) == 2:
            while len(ins) < 4:
                ins = '0' + ins
        ret.append(ins)

    return ":".join(ret)


def check_time_delta_less_one(t):
    t = t.split(":")
    return t[0] == '00' and t[1] == '00' and float(t[2]) < 2.00

def outage_data(arr):
    arr.sort()
    N = len(arr)
    
    for i in range(N - 1):
        t1, t2 = arr[i], arr[i + 1]
        #print(t1, t2, subtract_times(t1, t2))
        if(not check_time_delta_less_one(subtract_times(t1, t2))):
            print(t1 + '-' + t2)


def moves(N, sr, sc, er, ec, bishop_r, bishop_c):
    dirs = [(2, 1), (1, 2), (-2, 1), (2, -1), (-1, 2), (1, -2), (-1, -2), (-2, -1)]

    def in_bounds(testr, testc):
        return testr >= 0 and testc >= 0 and testr < N and testc < N

    def in_danger_by_bishop(testr, testc):
        return testr + testc == bishop_r + bishop_c or testc - testr == bishop_c - bishop_r

    q = [(sr, sc, False, [(sr, sc, False)])]
    visited = set([(sr, sc, False)])

    while q:
        newq = []
        for item in q:
            r, c, captured_bishop, testing = item
            if (r, c) == (er, ec): return testing, len(testing) - 1

            for dr, dc in dirs:
                newr, newc = dr + r, dc + c

                if not in_bounds(newr, newc): continue

                next_captured_bishop = (captured_bishop or (newr, newc) == (bishop_r, bishop_c))

                if in_danger_by_bishop(newr, newc) and not next_captured_bishop and not (newr, newc) == (er, ec): continue

                if (newr, newc, next_captured_bishop) in visited: continue
                visited.add((newr, newc, next_captured_bishop))
                newq.append((newr, newc, next_captured_bishop, testing + [(newr, newc, next_captured_bishop)]))
        q = newq
    return -1


# COPY EVERYTHING ABOVE

if __name__ == '__main__':
    # print(moves(6, 0, 0, 0, 2, 0, 1))
    # print(moves(8, 4, 2, 2, 6, 2, 3))
    print(moves(10, 9, 9, 6, 3, 7, 4))
    # i1 = ['12:31:04.04', '12:31:05.01', '12:31:06.21', '12:31:14.39',
    # "12:31:15.13", "12:31:16.98", "12:31:17.09"]
    # outage_data(i1)
    # print(subtract_times("14:44:59.52", "14:45:00.50"))
    # print(subtract_times("00:31:59:59", "00:32:00:01"))
    # print(subtract_times("00:31:59:59", "00:32:59:59"))
    # print(subtract_times("00:31:59:59", "00:32:01:10"))