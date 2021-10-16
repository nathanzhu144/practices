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
    user_to_activation_time = dict()
    bot_table = collections.Counter()
    is_bot = set()

    for invite in invites:
        timestamp, event_type, email = invite.split(',')

        if event_type == 'invite_requested':
            if email not in user_to_first_req:
                user_to_first_req[email] = int(timestamp)
            
            # check for bot
            bot_key = make_time_tuple_minute(timestamp, email)
            bot_table[bot_key] += 1
            if bot_table[bot_key] == 5:
                is_bot.add(email)
        elif event_type == 'invite_sent':
            did_user_invite_get_sent.add(email)
        elif event_type == 'invite_activated':
            if email in did_user_invite_get_sent and email in user_to_first_req:
                user_to_activation_time[email] = int(timestamp)
    
    num_actual_users = 0
    tot = 0
    for user in user_to_activation_time:
        if user in is_bot: continue
        if user not in did_user_invite_get_sent or user not in user_to_first_req: continue
        tot += user_to_activation_time[user] - user_to_first_req[user]
        num_actual_users += 1

    return len(is_bot), 0 if num_actual_users == 0 else tot // num_actual_users


    buckets = []

# COPY EVERYTHING ABOVE

if __name__ == '__main__':
    print(process_invites(['1618837700,invite_requested,jane@gmail.com', '1618837701,invite_sent,jane@gmail.com', '1618837702,invite_activated,jane@gmail.com']))
    print(process_invites(['1618837692,invite_requested,john@gmail.com', '1618837703,invite_requested,jane@gmail.com', '1618837711,invite_activated,john@gmail.com', '1618837723,invite_sent,john@gmail.com', '1618837745,invite_sent,jane@gmail.com', '1618837899,invite_activated,jenny@gmail.com', '1618837902,invite_activated,johnny@gmail.com', '1618837913,invite_requested,jenny@gmail.com']))
    print(process_invites(['1618837800,invite_requested,bot@gmail.com', '1618837801,invite_requested,bot@gmail.com', '1618837802,invite_requested,bot@gmail.com', '1618837803,invite_requested,bot@gmail.com', '1618837804,invite_requested,bot@gmail.com', '1618837805,invite_sent,bot@gmail.com', '1618837806,invite_activated,bot@gmail.com']))
    print(process_invites(['1618837692,invite_requested,john@gmail.com', '1618837693,invite_requested,john@gmail.com', '1618837694,invite_requested,jane@gmail.com', '1618837695,invite_requested,john@gmail.com', '1618837696,invite_requested,john@gmail.com', '1618837740,invite_requested,john@gmail.com', '1618837741,invite_requested,john@gmail.com', '1618837742,invite_requested,john@gmail.com', '1618837743,invite_requested,john@gmail.com', '1618837902,invite_sent,jane@gmail.com', '1618837905,invite_sent,john@gmail.com', '1618837912,invite_activated,john@gmail.com', '1618837977,invite_activated,jane@gmail.com']))