#include <iostream>

using namespace std;

#define ci 1000000007

long long pow(long long a,long long b){
    if (b==1){
        return a % ci;
    }else if(b%2==0){
        long long c = pow(a,b/2) % ci;
        return (c*c) % ci;
    }else{
        long long c = pow(a,(b-1)/2) % ci;
        return (((c*c)%ci) * a)%ci; 
    }
}


int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    int n,k;

    cin >> n >> k;

    long long fac[n+1];

    fac[0] = 1;
    fac[1] = 1;

    for(int i=2;i<n+1;i++){
        fac[i] =(fac[i-1] * i) % ci;
    }
    cout << (fac[n] * (pow((fac[n-k] * fac[k])%ci,ci-2) % ci))%ci;


}