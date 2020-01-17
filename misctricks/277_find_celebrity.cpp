/**  Nathan Zhu
 *   Leetcode 277 | medium | med
 *   Category: O(N^2) time not bad, O(N) time kinda requires insight.
 */
bool knows(int a, int b);

int findCelebrity(int n) {
    int left = 0, right = n - 1;
    while(left < right){
        if(knows(left, right)){
            left++;
        }
        else if(knows(right, left)){
            right--;
        }
        else if(!knows(left, right) && !knows(right,left)){
            left++;
            right--;
        }
    }
    
    
    for(int i = 0; i < n; ++i){
        if(i == left) continue;
        // If left knows i, this is not a celebrity
        // If i doesn't know left, this is not a celebrity
        if(knows(left, i) || !knows(i, left)) return -1;
    }
    return right;
}