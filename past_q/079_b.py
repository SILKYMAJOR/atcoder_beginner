#include <bits/stdc++.h>
using namespace std;
int main(){
  int64_t Ln_1 = 2;
  int64_t Ln = 1;
  int n = 0;
  int64_t tmp =0;
  
  cin >> n;
  
  if(n == 1){
    cout << 1 << endl;
  }else{
    for(int i=0;i<n-1;i++){
        tmp = Ln;
        Ln = Ln + Ln_1;
        Ln_1 = tmp;
    }
    cout << Ln << endl;
  }
  
}

