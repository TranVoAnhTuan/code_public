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
  ll ans = 0;
  while(n > 0){
    n /= 5;
    ans += n;
  }
  cout << ans;
  return 0;
}
