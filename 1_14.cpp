#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int A, B, C, imax, imin;
  cin >> A >> B >> C;
  
  imin = min(A, min(B, C));
  imax = max(A, max(B, C));
  
  cout << imax - imin << endl;
}

