# Nathan Zhu 11:03 pm Napa Valley December 26th, 2019 
# Leetcode 638 | medium | medium
# Category: DP
# 
# We do dp on needs array, turning it into a tuple.  
# Since we have a baseline price for each of the items, we know a rough minimum cost,
# without using any special offers is just the dot product of price and needs array.
#

def shoppingOffers(price, special, needs):
    """
    :type price: List[int]
    :type special: List[List[int]]
    :type needs: List[int]
    :rtype: int
    """
    table = dict()
    def helper(needs):
        key = tuple(needs)
        if key in needs: return table[key]

        # Our base case for this function is not apparent, but actually works because
        # when we have nothing in needs, as in needs is all zeroes, we cannot take any deals,
        # so we return 0.

        # This is a baseline price that we can get. 
        ret = 0
        for i in range(len(price)):
            ret += price[i] * needs[i]

        # We see what new prices we can get by taking a special.
        for offer in special:
            for i, need in enumerate(needs):
                if need < offer[i]:
                    break
            # else runs only if break doesn't occur, as in we can take this offer.
            else:
                new_needs = [need - offer[i] for i, need in enumerate(needs)]
                ret = min(ret, offer[-1] + helper(new_needs))

        table[key] = ret
        return ret

    return helper(needs)   

if __name__ == "__main__":
    shoppingOffers([1,1,1], [[1,1,1,0], [2,2,1,1]], [1,1,0])