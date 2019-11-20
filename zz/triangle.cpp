#include <iostream>
#include <vector>


using namespace std;

class Shape{
public:
    Shape(){}
    virtual void print_area() = 0;
};

class Triangle : public Shape{
    void print_area() override{
        cout << "Tri" << endl;
    }
};

class Iso : public Triangle{
    void print_area() override{
        cout << "Iso" << endl;
    }
};


class Node{
public: 
    Node(int val_in) : val(val_in), next(nullptr) {}
    Node* next;
    int val;
};

Node * make_nodes(vector<int> v, int i){
    if(i < v.size()){ 
        Node* n = new Node(v[i]);
        n->next = make_nodes(v, i + 1);
        return n;
    }
    else{
        return nullptr;
    }
}

void print_n(Node* n){
    for(Node* i = n; i != nullptr; i = i->next){
        cout << i->val << " ";
    }
    cout << endl;
}


int main(){
    vector<int> f = {};
    vector<int> s = {1, 2, 3};  //insert 4

    Node* first = make_nodes(f, 0);
    Node* sec = make_nodes(s, 0);
}
