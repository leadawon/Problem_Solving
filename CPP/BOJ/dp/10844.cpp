#include <iostream>

using namespace std;

int main(void){
    int n;
    cin >> n;
    long long dp[10][n];

    for(int i=1;i<10;i++){
        dp[i][0] = 1;
    }
    dp[0][0] = 0;

    for(int k=1;k<n;k++){
        dp[0][k] = dp[1][k-1];
        dp[9][k] = dp[8][k-1];
        for(int i=1 ; i<9 ; i++){
            dp[i][k] = dp[i-1][k-1] + dp[i+1][k-1];
            dp[i][k] = dp[i][k] % 1000000000;
        }
    }
    //cout << 1000000000 << endl;
    long long cnt=0;

    for(int i=0;i<10;i++){
        cnt+=dp[i][n-1] % 1000000000;
    }

    cout << cnt%1000000000 << endl;

}