#include <iostream>
#include <string>
#include <vector>

using namespace std;

int foo(int x, string y){
    return 5;
}

int (*fctPtr1)(int, string) = foo;

bool (*comparisonFcn)(int, int) a;


vector< vector<int> > vect{ {1, 2, 3},
                            {4, 5, 6}};

vector< vector<int> > array_2d(rows, vector<int>(cols, 0));

if(c.find("key") != c.end()){
    string key = c.find("key")->first;
    string sec = c.find("val")->val;
}