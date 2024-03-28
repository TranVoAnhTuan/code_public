#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
const int maxV = 1e6+1;
ll n;
queue<int>solve(int n){
  queue<int> permutation;
  if(n == 1){
    permutation.push(1);
  }
  else if(n == 2 || n == 3){
  }
  else{
    for(ll i = 2; i <= n; i += 2){
      permutation.push(i);
    }
    for(ll i = 1; i <= n; i += 2){
      permutation.push(i);
    }
  }
  return permutation;
}

int main(){
  cin>>n;
  queue<int> ans = solve(n);
  if(ans.empty()){
    cout<< -1 ;
  }
  else{
    while(!ans.empty()){
      cout << ans.front() << " ";
      ans.pop();
    }
  }
  return 0;
}
