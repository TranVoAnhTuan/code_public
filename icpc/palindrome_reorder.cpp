#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
const int maxV = 1e6+1;
string str;
int main(){
  IOS;
  // freopen("test.inp", "r", stdin);
  // freopen("test.out", "w", stdout);
  cin >> str;
  ll f[26]= {0}, mark = -1;
  fi(i, 0, str.length()-1){
    f[str[i]-'A']++;
  }
  fi(i, 0, 25){
    if(f[i]%2){
      if(mark != -1 ){
        cout << "NO SOLUTION";
        return 0;
      } else{
        mark = i;
      }
    }
  }
  fi(i, 0, 25){
    fi(j, 0, f[i]/2 - 1){
      cout<< ((char)(i+'A'));
    }
  }
  if(mark != -1){
    cout << ((char)(mark+'A'));
  }
  fd(i, 25, 0){
    fi(j, 0, f[i]/2 -1){
      cout << ((char)(i+'A'));
    }
  }
  return 0;
}
