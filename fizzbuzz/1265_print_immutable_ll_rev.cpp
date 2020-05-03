
/* Nathan Zhu April 28th, 2020 EECS 376 exam soon.
*  Leetcode 1265 | medium | easy?
*  Category: fizzbuzz
*/

class ImmutableListNode{
public:
    void printValue(){}
    ImmutableListNode* getNext(){ return nullptr; }
};
void printLinkedListInReverse(ImmutableListNode* head) {
    if(!head) return;
    printLinkedListInReverse(head->getNext());
    head->printValue();
    
}