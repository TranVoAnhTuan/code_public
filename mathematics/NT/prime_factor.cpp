#include<bits/stdc++.h>
using namespace std;
int n;
int main(){
    cin >> n;
    int tmp = n;
    for(int i = 2; i <= sqrt(n); i++){
        int exponent = 0;
        while(tmp % i == 0){
            exponent++;
            tmp /= i;
            if(tmp % i != 0){
                cout << i << "^" << exponent;
                if(tmp != 1){
                    cout << "*";
                }
            }
        }

    }
    if(tmp > 1){
        cout << "so nguyen to";
    }
    cout << endl;
    return 0;
}