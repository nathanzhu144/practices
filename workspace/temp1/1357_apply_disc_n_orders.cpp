
#include <unordered_map>


class Cashier {
private:
    int n, curr, discount;
    unordered_map<int, int> table;
public:
    Cashier(int n, int discount, vector<int>& products, vector<int>& prices) {
        this->n = n;
        curr = 0;
        this->discount = discount;
        for(int i = 0; i < products.size(); ++i){
            table[products[i]] = prices[i];
        }
    }
    
    double getBill(vector<int> product, vector<int> amount) {
        double amt = 0;
        for(int i = 0; i < product.size(); ++i){
            amt += (amount[i] * table[product[i]]);
        }
        
        curr++;
        if(curr == n){
            curr = 0;
            return amt - (discount * amt) / 100.0;
        }
        else return amt;
    }
};