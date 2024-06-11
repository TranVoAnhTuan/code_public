#include <bits/stdc++.h>
#include <set>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define MOD 1000000007
const int maxV = 1e6+1;
set<string> solve(string a, int l, int r) 
{ 
  set<string> permutations;  
  if (l == r) {
    permutations.insert(a);  
  } else {
  fi(i, l, r){
    swap(a[l], a[i]);
    set<string> subPermutations = solve(a, l + 1, r);
    permutations.insert(subPermutations.begin(), subPermutations.end());
    swap(a[l], a[i]);
    }
  }
  return permutations;  
}
int main(){
  IOS;
  string str;
  cin >> str;
  int n = str.size(); 
  set<string> permutations = solve(str, 0, n - 1);
  cout << permutations.size() << '\n';
  for (string ans : permutations) {
    cout << ans << '\n';
  }
  return 0;
}

