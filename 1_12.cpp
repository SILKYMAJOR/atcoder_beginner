#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;
  int num = 1;

  for(int i=0;i<S.size() - 1;i++){
    i++;
    char c =  S.at(i);
    char plus = '+';
    char minus = '-'; 
    
    if(c == plus){
      num++;
    }
    else if(c == minus){
      num--;
    }
  }
  cout << num << endl;
}
