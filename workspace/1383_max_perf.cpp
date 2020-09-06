Intuition
Doesn't efficiency and speed are the same thing?
Like efficiency = speed = produce / time?
Speed sounds more like time actually.
You work slow, so you need more time.


There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers. 

 

Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4)
 and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.


    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        vector<pair<int, int>> ess;
        for (int i = 0; i < n; ++i)
            ess.emplace_back(efficiency[i], speed[i]);
        sort(rbegin(ess), rend(ess));
        long sumS = 0, res = 0;
        priority_queue <int, vector<int>, greater<int>> pq; //min heap
        for(auto& [e, s]: ess){
            pq.emplace(s);
            sumS += s;
            if (pq.size() > k) {
                sumS -= pq.top();
                pq.pop();
            }
            res = max(res, sumS * e);
        }
        return res % (int)(1e9+7);
    }