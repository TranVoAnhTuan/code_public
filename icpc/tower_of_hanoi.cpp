#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MOD 1000000007
const int maxV = 1e6+1;
int n;
void solve(int l, int mid, int r, int n){
  if(n == 0){
    return;
  }
  solve(l, r , mid , n-1);
  cout << l << '\t' << r << '\n';
  solve(mid, l , r, n-1);
}
int main(){
  IOS;
  cin >> n;
  cout << (1 << n) - 1 << '\n';
  solve(1, 2, 3, n);
  return 0;
}

