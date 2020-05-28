

/** May 10th, 2020, Stockton, CA.  First day at work, 10:54 pm.  We did mostly orientations today, but first day at work!!
 *  Leetcode 1305 | medium | medium
 *  Category: Tree
 *  Runtime O(N), space O(N)
 * 
 *  This is inorder BST iterative on steroids!
 * 
 *  Honestly, it feels like everything is coming full-circle.  It was more or less two weeks to the day that I start work in New York.  It was three days ago when
 *  we had our trip in california with Hershal and crew.  It was before work on that first day at Amex that I really started doing leetcode.  I think I started from
 *  maybe 30 questions done or something?  I was laughably bad, but at some point since I always did leetcode at lunch, everyone came to think I was pretty good.  
 * 
 *  I haven't comped the latest couple days, but I'm definitely within hitting range of doing 1000 questions total this year.  My counter says 939 not including the work of the last 
 *  3 days, and there was one day where I did at least 10 questions.  If I can do 50 questions in the next two weeks, I can hit 1000 qs done.  That's damn doable, and 
 *  I can get that done.
 * 
 */



#include <unordered_map>
#include <vector>
using namespace std;


class TreeNode {
public:
    TreeNode(int n){ val = n; }
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode* parent;
};


vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
    vector<int> ret;
    vector<TreeNode*> stk1, stk2;
    
    while(stk1.size() || stk2.size() || root1 || root2){
        while(root1){
            stk1.push_back(root1);
            root1 = root1->left;
        }
        
        while(root2){
            stk2.push_back(root2);
            root2 = root2->left;
        }
        
        if((stk1.size() && stk2.size() && stk1.back()->val <= stk2.back()->val) || (stk1.size() && !stk2.size())){
            root1 = stk1.back();
            stk1.pop_back();
            ret.push_back(root1->val);
            root1 = root1->right;
        }
        else{
            root2 = stk2.back();
            stk2.pop_back();
            ret.push_back(root2->val);
            root2 = root2->right;
        }
    }
    
    return ret;
}