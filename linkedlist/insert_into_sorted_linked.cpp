#include <iostream>

using namespace std;

class Node{
    public:
    int val;
    Node* next;
};

Node* add_node(Node *n, int val_in){
    Node *a = new Node;
    a->val = val_in;
    a->next = nullptr;

    if(n == nullptr){
        return a;
    }
    
    Node *end = n;
    while(end->next != nullptr){
        end = end->next;
    }

    end->next = a;
    return n;
}

////////////////////////////////////////
//           Solution                 //
////////////////////////////////////////
/*
*   Basic intuition:
*     We have two pointers, one previous and one current
*
*          2  ->  5  ->  9  ->  nullptr
*                 ^prev  ^curr
*
*           insert(7) on list
*
*           make a newnode 7
*           newnode->next = curr
*           prev->next = newnode
*  
*   There are three major cases.
*   1. insert at beginning of list
*       - note this includes case where ll is empty (tricky),
*         this code doesn't work if we handle case 3 first
*       - in this case, we have to be careful to change head of 
*         list, as head of list actually beecomes our inserted node
*   2. we insert into inside of list
*       - standard
*   3. insert at end of list
*       - do everything, except newnode->next is nullptr
*/

//      HARDER WAY
//returns head node
Node* insert_into_sorted(Node* list, int val){
    Node *prev = nullptr;
    Node *curr = list;

    while(curr != nullptr && val > curr->val){
        //orderering of these 2 lines are important//
        prev = curr;
        curr = curr->next;
    }

    // insert(2) into 5 -> 7 -> 9 -> nullptr
    //                2  ->  5  ->  7 -> 9 -> nullptr
    // in this case we insert before
    // prev is nullptr iff we exit while loop immediately
    if(prev == nullptr){
        Node *temp = new Node;
        temp->val = val;
        temp->next = list;
        list = temp;  //insert before ll, so we return temp
        return list;
    }
    // in this case we insert after ll
    // curr is nullptr iff val < curr->val is never false,
    // so we know added val is bigger than all other values
    else if(curr == nullptr){
        Node *temp = new Node;
        temp->val = val;
        temp->next = nullptr;
        prev->next = temp;    //prev should be end of list
        return list;
    }
    //this case is standard case where we insert into a ll
    //insert(3)  into -1 -> 2 -> 4 -> nullptr
    else{
        Node *temp = new Node;
        temp->val = val;
        temp->next = curr;
        prev->next = temp;   
        return list;
    }
}

//  Note: Having a dummy makes this process much easier.
 //EASIER WAY
 //                dummy(-1) ->  -5  ->  7 -> 9 -> nullptr
 //                dummy(-1) ->  nullptr
 //                dummy(-1) ->  -3  ->  nullptr         
 //  There is only one case, with dummy.

Node* insert_into_sorted_dummy(Node* list, int val){
    Node *dummy = new Node;
    dummy->val = -1;
    dummy->next = list;
    list = dummy;

    Node *prev = list;         //prev starts on dummy
    Node *curr = list->next;   //we have a dummy
    while(curr != nullptr && val > curr->val){
        //ordering of these 2 lines are important//
        prev = curr;
        curr = curr->next;
    }

    Node *temp = new Node;
    temp->val = val;
    temp->next = curr;
    prev->next = temp;

    return list->next;
}

void print_list(Node* l){
    if(l == nullptr){
        return;
    }
    cout << l->val << " ";
    print_list(l->next);
}

int main(){
    Node* l1 = nullptr;

    l1 = insert_into_sorted(l1,1);
    l1 = insert_into_sorted(l1,5);
    l1 = insert_into_sorted(l1,-1);
    l1 = insert_into_sorted(l1,3);

    print_list(l1);
    cout << endl;

    Node* l2 = nullptr;

    l2 = insert_into_sorted_dummy(l2,1);
    l2 = insert_into_sorted_dummy(l2,5);
    l2 = insert_into_sorted_dummy(l2,-1);
    l2 = insert_into_sorted_dummy(l2,3);
    print_list(l2);


}