#  8:27 am Amex building, New York, NY, 36th floor, cubicle 202 B.  
#  Leetcode 115 | hard | hard??  lol
#  Category: DP, similar thinking as LCS
#  
#  Getting some warming up done before work.
# 
#  Given a string src and a string dest, count the number of distinct subsequences of src which equals dest.
#
#  Recursive step:
#     If, last char of src and dest are same, it is possible that the last character of src is used as part of a subsequence that
#     will match dest.  It is also possible it is not used as part of a subsequence that will match dest. Therefpre, total subsequences
#     that match dest is the sum of these two possibilities.
#
#        num_dist_subseq(src, dest, src_index, dest_index) = num_dist_subseq(src, dest, src_index - 1, dest_index - 1)    <- last char of src is used for matching last of dest
#                                                          + num_dist_subseq(src, dest, src_index, dest_index - 1)        <- last char of src is NOT used to match last char of dest
#
#     Else, it is impossible last character of src is used as a part of a subsequence that will match dest.  
#        
#        num_dist_subseq(src, dest, src_index, dest_index) = num_dist_subseq(src, dest, src_index - 1, dest_index - 1)  
#                                                            ^-- last char of src is NOT used to match last char of dest, so we just discard it
#
#  Base case:
#     If we get to a -1 index for src or dest, we can determine whether we successfully found a matching subsequence by
#     checking whether index of dest is -1.  Index of dest is -1 iff we have matched the whole sequence
#     
# 

def helper(src, dest, index_src, index_dest, mem):
    key = (index_src, index_dest)

    if key in mem:
        return mem[key]

    #base case
    if index_src == -1 or index_dest == -1:
        mem[key] = 0 + (index_dest == -1)        #mem[key] should be 1 iff index_dest is 0, 0 + for casting purposes

    #last two chars match
    elif src[index_src] == dest[index_dest]:
        mem[key] = helper(src, dest, index_src - 1, index_dest - 1, mem) + helper(src, dest, index_src - 1, index_dest, mem)
    #last two chars don't match
    else:
        mem[key] = helper(src, dest, index_src - 1, index_dest, mem)
    
    return mem[key]

def num_dist_subsequences(src, dest):
    mem = {}
    return helper(src, dest, len(src) - 1, len(dest) - 1, mem)


if __name__ == "__main__":
    print(num_dist_subsequences("rabbbit", "rabbit"))   # should be 3
    print(num_dist_subsequences("rabbit", "rabbit"))   # should be 1
    print(num_dist_subsequences("babgbag", "bag"))   # should be 5