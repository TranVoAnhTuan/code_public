#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
const int maxV = 1e6+1;
ll n;
int main(){
  IOS;
  cin >> n;
  if(n == 1){
    cout << "NO";
  }
  else if(n == 2){
    cout << "NO";
  }
  // else if((n*(n+1))/2 % 2){
  //   cout << "YES";
  // }
  else if(n % 4 == 0 || n % 4 == 3){
    cout << "YES";
  }
  else{
    cout << "NO";
  }
  return 0;
}
