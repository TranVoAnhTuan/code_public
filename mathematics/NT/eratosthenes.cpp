#include<bits/stdc++.h>
using namespace std;
const int maxN = 1e6+1;
vector<bool> prime(maxN, true);
int main(){
    prime[0] = prime[1] = false;
    for(int i = 2; i <= sqrt(maxN); i++){
        if(prime[i]){
            for(int j = i * i; j <= maxN; j += i){
                prime[j] = false;
            }
        }
    }
    int test;
    cin >> test;
    cout << prime[test] << '\n';
    return 0;
}