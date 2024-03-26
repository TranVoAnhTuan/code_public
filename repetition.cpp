#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fi(i,a,b) for(ll i = a; i <= b; i++)
#define fd(i,a,b) for(ll i = a; i >= b; i--)
#define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
const int maxV = 1e6+1;
string str;
int maxStr(string str){
  int currMax = 0, currLen = 1;
  char currStr = str[0];
  fi(i,1,str.size()-1){
    if(str[i] == currStr){
      currLen++;
    }
    else{
      currMax = max(currMax, currLen);
      currLen = 1;
      currStr = str[i];
    }
  }
  currMax = max(currMax, currLen);
  return currMax;
}
int main(){
  IOS;
  cin>>str;
  cout<<maxStr(str);
  return 0;
}
