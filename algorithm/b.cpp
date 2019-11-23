#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, K;
  int count = 0;
  int high=0;
  
  cin >> N >> K;
  for(int i=0;i<N;i++){
    cin >> high;
    if(high>=K){
      count++;
    }
  }
  cout << count << endl;
  return 0;
}

