def most_freq_subtree_sum(root):
    
    def helper(root):
        if not root: return 0
        