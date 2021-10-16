import collections
from datetime import datetime, time

def same_minute(time, timee):
    dt = datetime.fromtimestamp(time)
    dtt = datetime.fromtimestamp(timee)
    #print(dt, dtt)
    return (dt.year == dtt.year) and (dt.month == dtt.month) and (dt.day == dtt.day) and (dt.hour == dtt.hour) and (dt.minute == dtt.minute)

def make_time_tuple_minute(time, email):
    dt = datetime.fromtimestamp(int(time))
    return (dt.year, dt.month, dt.day, dt.hour, dt.minute, email)
    
# subtracts two times, finds diff
def process_invites(invites):
    user_to_first_req = dict()
    did_user_invite_get_sent = set()

# JP Morgan one
def is_good(num):
    num = str(num)
    c = collections.Counter(num)

    for i, ch in enumerate(num):
        ch_we_want = str(i)
        num_occur = int(ch)
        if c[ch_we_want] != num_occur:
            print('0')
            return
        del c[ch_we_want]
    print('1') if not c else print('0')

# 

def find_nums(arr):
    numerals = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    cts = [collections.Counter(item) for item in numerals]

    c = collections.Counter(arr)
    ret = []
    dog = [[]]

    def helper(num_we_are_removing):
        if num_we_are_removing >= 10:
            return False
        if not c:
            dog[0] = ret[:]
            return True
        
        can_remove = True
        for ch, ct in cts[num_we_are_removing].items():
            # not enough chars in jumbled string
            # move onto next bigger number
            if ch not in c or ct > c[ch]:
                can_remove = False
                break
        
        if not can_remove:
            helper(num_we_are_removing + 1)
        else:
            for ch, ct in cts[num_we_are_removing].items():
                c[ch] -= ct
                if c[ch] == 0: del c[ch]
            ret.append(num_we_are_removing)

            if not helper(num_we_are_removing):
                for ch, ct in cts[num_we_are_removing].items():
                    c[ch] += ct
                ret.pop()
                helper(num_we_are_removing + 1)
                
    helper(0)
    return "".join(map(str, dog[0]))

print(find_nums('reuonnoinfe'))
#print(find_nums('onetwo'))

# print(is_good('2020'))
# print(is_good('22'))