# Nathan Zhu 10:50 pm Monday Dec 30th, 2019, Santa Cruz hotel
# Leetcode 923 | medium | damn hard yoooo
# Category: Misc tricks
# The insight is simple, the edge cases are annoying.
# So, the basic idea is that we are trying to find the total number of triplet indices which add up to target.
# 
# We use basic counting theory to make a N^2 soln run a lot faster.
# This is a good problem, thought.
#
def threeSumMulti(self, A, target):
    """
    :type A: List[int]
    :type target: int
    :rtype: int
    """
    A.sort()
    N = len(A)
    
    ret = 0
    for first in range(N - 2):
        sec, third = first + 1, N - 1
        while sec < third:
            if A[first] + A[sec] + A[third] < target: sec += 1
            elif A[first] + A[sec] + A[third] > target: third -= 1
            else:
                # We want to track how far right sec moves and how far left third moves
                # There are 2 cases, 
                # 1. A[sec] < A[third]
                # Suppose
                #        1  1  1  2  4  4  4
                #       sec                  third
                #                sec+3
                #                third-2
                #           NOTE indices can overlap.
                #
                # Total pair is 3 * 2 == sec_m * third_m
                #
                # 2. A[sec] == A[third]
                # Suppose
                #        3  3  3  3  3
                #       sec          third
                #                    sec_m
                #                    third_m
                #
                # sec_m = 3
                # third_m = 0
                # Total pair is C(5, 2) == C(sec_m + third_m + 1, 2) == (sec_m + third_m + 1) * (sec_m + third_m) / 2
                sec_m, third_m = 1, 1
                while sec + sec_m < third and A[sec] == A[sec + sec_m]: sec_m += 1
                while sec + sec_m <= third - third_m and A[third] == A[third - third_m]: third_m += 1
                    
                if A[sec] != A[third]: ret += sec_m * third_m
                else: ret += (sec_m + 1) * sec_m / 2
                sec += sec_m
                third -= third_m
    return ret % (10 ** 9 + 7)
                


# Faster than 28% of C++ submissions
# Python is slightly too slow (passes all test cases, but too slow?)
# int threeSumMulti(vector<int>& A, int target) {
#     sort(A.begin(), A.end());
    
#     long ret = 0;
#     int N = A.size();
    
#     for(int first = 0; first < N; ++first){
#         int sec = first + 1;
#         int third = N - 1;
#         while(sec < third){
#             if(A[first] + A[sec] + A[third] > target) third--;
#             else if(A[first] + A[sec] + A[third] < target) sec++;
#             else{
#                 int l = 1;
#                 int r = 1;
#                 while(sec + l < third and A[sec] == A[sec + l]) ++l;
#                 while(sec + l <= third - r and A[third] == A[third - r]) ++r;
                
#                 ret += A[sec] == A[third] ? (l + 1) * l / 2 : l * r;
#                 sec += l;
#                 third -= r;
#             }
#         }
#     }
#     return ret % 1000000007;
# }