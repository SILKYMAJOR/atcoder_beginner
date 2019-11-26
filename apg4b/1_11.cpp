#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, A;
  int count = 1;

  cin >> N >> A;

  while(count <= N){
    string fao;
    int num;
    cin >> fao >> num;
    
    if(fao == "+"){
      A = A + num;
    }
    else if(fao == "-"){
      A = A - num;
    }
    else if(fao == "*"){
      A = A * num;
    }
    else if(fao == "/"){
      if(num == 0){
        cout << "error" <<endl;
        return 0; 
      }
      A = A / num;
    }
    cout << count << ":" << A << endl;
    count++;
  }
}

