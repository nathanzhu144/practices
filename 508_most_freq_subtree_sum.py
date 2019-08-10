    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # calculates sum at every root.
        def calculate_tree_sum(root):
            if not root: return 0
            node_to_sum[root] = root.val + calculate_tree_sum(root.left) + \
                                           calculate_tree_sum(root.right)
            return node_to_sum[root]
        
        def init_most_common(root):
            if not root: return
            most_common[node_to_sum[root]] += 1
            init_most_common(root.left)
            init_most_common(root.right)
        
        if not root: return []
        node_to_sum = dict()                               # root -> sum of tree at this root
        most_common = collections.defaultdict(lambda: 0)   # val -> num of occur
        calculate_tree_sum(root)
        init_most_common(root)
        ret = []
        
        val = list(most_common.values())   # counts of each val
        keys = list(most_common.keys())    # val corresponding to count
        largest_val_index = val.index(max(val))
        for i in range(len(keys)):
            if most_common[keys[i]] == most_common[keys[largest_val_index]]: ret.append(keys[i])
        
        return ret