/** Nathan Zhu At home with Renying and there is a party going on - doing leetcode.  All is good in the world.  Dec 24th, 2019 7:13 pm
 *  Leetcode 445 | medium | medium 
 *  
 *  The regular add two numbers II involves both of the linked lists being reversed in the beginning.
 *  Suppose we reverse the linked lists, the 
 *  
 */
 #include <stack>
 
 using namespace std;
 
 struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    stack<int> first;
    stack<int> second;
    
    ListNode* f;
    for(f = l1; f; f = f->next) first.push(f->val);
    for(f = l2; f; f = f->next) second.push(f->val);
    
    int carry = 0;
    ListNode* ret = nullptr;
    
    while(!first.empty() || !second.empty()){
        int sum = 0;
        if(!first.empty()){
            sum += first.top();
            first.pop();
        }
        if(!second.empty()){
            sum += second.top();
            second.pop();
        } 
        
        sum += carry;
        
        ListNode* n = new ListNode(sum % 10);
        carry = sum / 10;
        n->next = ret;
        ret = n;
    }
    
    // If there is a carry bit
    if(carry){
        ListNode* n = new ListNode(1);
        n->next = ret;
        ret = n;
    }
    return ret;
}