/** Nathan Zhu 
 *  Leetcode 222 | medium | ehhh not so easy
 *  I think the insight to this problem isn't that easy.
 *  
 *  You use the height of left and right subtree to figure out if either of the two
 *  is a complete tree.  This is a log(N) solution.
*/

public int height(TreeNode root){
    if(root == null) return 0;
    return 1 + height(root.left);
}

public int countNodes(TreeNode root) {
    if(root == null) return 0;
    
    int left = height(root.left);
    int right = height(root.right);
    
    if(left == right) return (1 << (left)) + countNodes(root.right);
    else return (1 << (right)) + countNodes(root.left);
}