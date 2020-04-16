/* Nathan Zhu Saturday Feb 29th, 2020. Founrdy Lofts, Michael just left for spring break.  Hershal and Peifu are leaving Monday for Nashville.
*  Leetcode 829 | hard | damn cool
*  Cateogory: Math
*
*  Note, given a sequence of N inc numbers, here's the numbers we can make from them.
*
*  1 + 2 + 3 + ... + N     == 1 + 2 + 3 + ... + N
*  2 + 3 + 4 + ... + N + 1 == 1 + 2 + 3 + ... + N + N
*  2 + 3 + 4 + ... + N + 2 == 1 + 2 + 3 + ... + N + N + N
* ...
*
*  Therefore, we can tell if a number can be composed of N inc numbers in O(1) time.
*/
    
int calc_sum(int n){ return (n * (n + 1)) / 2;}

int consecutiveNumbersSum(int N) {
    int ret = 0;
    for(int i = 1; calc_sum(i) <= N; ++i){
        if((N - calc_sum(i)) % i == 0) ret++;
    }
    return ret;
}
