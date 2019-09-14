Approach #1: Meet in the Middle [Accepted]
Intuition and Algorithm

First, let's get a sense of the condition that average(B) = average(C), where B, C are defined in the problem statement.

Say A (the input array) has N elements which sum to S, and B (one of the splitting sets) has K elements which sum to X.
 Then the equation for average(B) = average(C) becomes \frac{X}{K} = \frac{S-X}{N-K} 
K
X
​	
 = 
N−K
S−X
​	
 . This reduces to X(N-K) = (S-X)KX(N−K)=(S−X)K which is \frac{X}{K} = \frac{S}{N} 
K
X
​	
 = 
N
S
​	
 . That is, average(B) = average(A).

Now, we could delete average(A) from each element A[i] without changing our choice for B. (A[i] -= mu, where mu = average(A)). 
This means we just want to choose a set B that sums to 0.

Trying all 2^N2 
N
  sets is still too many choices, so we will create sets of sums left, right of the approximately 2^{N/2}2 
N/2
  choices on the left and on the right separately. (That is, left is a set of sums of every powerset in the first half of A, and right is the set of sums of every powerset in the second half of A). Then, it is true if we find 00 in these powersets, or if two sums in different halves cancel out (-x in right for x in left), except for one minor detail below.

Care must be taken that we do not specify sets that would make the original B or C empty. If sleft = A[0] + A[1] + ... + A[N/2 - 1], and sright = A[N/2] + ... + A[N-1], (where A[i] was transformed to the new A[i] - average(A)) then we cannot choose both (sleft, sright). This is correct because if for example sleft was a sum reached by a strictly smaller powerset than {A[0], A[1], ..., A[N/2 - 1]}, then the difference between these sets would be non-empty and have sum 0.