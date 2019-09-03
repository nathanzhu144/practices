# Nathan Zhu 10:02 am, Thurs, August 22, 2019.  
# Leetcode 358 | hard | hard this is kinda hard actually
# Category: PQ, This is similar to 621, task scheduler,.  Basically same actually.


# 1. We have a loop that runs for k iterations, where k is the cooldown of placing a character.
#    Cooldown meaning the distance between the same character.
#
#    We take a greedy approach, grabbing the largest character from the heap. That's the next
#    character we will use in our string.
# 
#    We then ban the character by putting it into the cooldown array, with the updated count
#    for having used the character once.  NOTE WE DON'T PUSH BACK INTO PQ, ESSENTIALLY BANNING IT.
#
# 2. We push all banned elements back into pq.
#
#
#    EXIT COND: If heap is empty return empty string if cooldown list is NOT EMPTY.  Means that
#               we still have characters to use, and it is impossible
#
#   Correctness questions:
# 
#   1. We don't enforce an ordering.  Since we push everything back into the cooldown array at the
#      same time, how do we know we won't choose the same task within k distance?
#  
#      This one is tricky. It is important to note that if the characters are k distance apart,
#      the ordering of choices in thte if loop are the same.  Suppose that they are not the same.
#      This means one or more characters in the if statement have counts lower than other counts in the pq.
#      This can only space out the characters by larger than k distance.
#
#      



def rearrangeString(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    # EDGE CASE, k == 0 means any ordering is OK
    if k == 0: return s
    
    c = collections.Counter(s)
    pq = list()
    ret = list()
    for character, count in c.items(): heapq.heappush(pq, (-1 * count, character))
    
    while True:
        cooldown = []
        
        # Replace 2 for K, we want K distance apart.
        for i in range(k):
            if not pq:
                # 
                if not cooldown: return "".join(ret)
                else: return ""
            
            count, next_char = heapq.heappop(pq)
            ret.append(next_char)
            if count < -1: cooldown.append((next_char, count + 1))
            
        for charac, count in cooldown:
            heapq.heappush(pq, (count, charac))


# C++ working code.

    # string rearrangeString(string s, int k) {
    #     if(k == 0) return s;
        
    #     unordered_map<char, int> counter;
    #     priority_queue<pair<int, char>> pq;
    #     string res;
        
    #     for(auto c: s) counter[c]++;
    #     for(auto c: counter) pq.push({c.second, c.first});
        
    #     while(true){
    #         vector<pair<int, char> > cooldown;
            
    #         for(int count = 0; count < k; ++count){
    #             if(pq.empty()){
    #                 if(cooldown.empty()) return res;
    #                 else return "";
    #             }
    #             pair<int, char> curr = pq.top();
    #             pq.pop();
    #             res += curr.second;
                
    #             if(curr.first > 1) cooldown.push_back({curr.first - 1, curr.second});
    #         }
            
    #         for(auto i: cooldown) pq.push(i);
    #     }
        
    # }