#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, lim_time;
  int min_cost = 0;
  
  int cost, time;
  cin >> N >> lim_time;
  
  for(int i=0;i<N;i++){
    cin >> cost >> time;
    if(lim_time>=time){
      if(min_cost == 0 || min_cost >= cost){
        min_cost = cost;
      }
    }
  }
  if(min_cost != 0){
    cout << min_cost << endl;
  }else{
    cout << "TLE" << endl;
  }
  return 0;
}

