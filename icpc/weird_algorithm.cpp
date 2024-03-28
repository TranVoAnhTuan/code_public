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
  // freopen("test.inp", "r", stdin);
  // freopen("test.out", "w", stdout);
  cin >> n;
  while(n != 1){
    if(n % 2 == 0){
      cout<< n <<" ";
      n /= 2;
    }
    else{
      cout << n << " ";
      n = n * 3 + 1;
    }
  }
  cout << 1;
  return 0;
}

