#include <iostream>

using namespace std;

class Node{
    public:
    int val;
    Node* next;
};

//How to find median of a linked list?
int find_median(Node* n){
    if(n == nullptr){
        return -1;
    }

    Node* fast = n;
    Node* slow = n;
    int counter = 0;

    while(++counter && fast->next != nullptr){
        fast = fast->next;
        if(counter % 2 == 1){
            slow = slow->next;
        }
    }

    if(counter % 2 == 0){
        return (slow->next->val + slow->val) / 2;
    }
    else{
        return slow->val;
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
    Node* l2 = nullptr;

    l2 = insert_into_sorted_dummy(l2,1);
    cout << find_median(l2) << endl;
    l2 = insert_into_sorted_dummy(l2,5);
    l2 = insert_into_sorted_dummy(l2,-1);
    l2 = insert_into_sorted_dummy(l2,3);
    cout << find_median(l2) << endl;

    l2 = insert_into_sorted_dummy(l2,3);
    cout << find_median(l2) << endl;


    print_list(l2);


}