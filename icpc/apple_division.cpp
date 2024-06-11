#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MOD 1000000007
const int maxV = 1e6+1;
ll a[20], n;
ll solve(ll* a, ll i, ll s1, ll s2, ll n){
  if(i > n){
    return abs(s1 - s2);
  }
  ll choose = solve(a, i + 1, s1 + a[i], s2, n);
  ll notChoose = solve(a, i + 1, s1, s2 + a[i], n);
  return min(choose, notChoose);
}
int main(){
  IOS;
  cin >> n;
  fi(i, 1, n){
    cin >> a[i];
  }
  cout << solve(a, 1, 0, 0, n);
  return 0;
}

