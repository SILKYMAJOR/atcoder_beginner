#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int num;
  int sum=0;
  int average=0;
 
  cin >> num;
  vector<int> atr(num);
  
  for(int i=0;i<num;i++){
    cin >> atr.at(i);
    sum = sum + atr.at(i);
  }
  average = sum/num;
  
  for(int i=0;i<num;i++){
    int difference = atr.at(i) - average;
    if(difference < 0) difference = difference * -1;
    cout << difference << endl;
  }
  
}
