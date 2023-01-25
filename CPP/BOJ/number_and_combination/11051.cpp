#include <iostream>

using namespace std;



int main(void){
    int n,r;
    cin >> n >> r;

    int dp[n+1][n+1]={0};
    dp[0][0] = 1;
    dp[1][0] = 1;
    dp[1][1] = 1;
    for(int i =2 ; i<=n;i++){
        for(int j=0;j<=i;j++){
            if (j == 0) {
                dp[i][0] = 1;
            }else if (j == i) {
                dp[i][j] = 1;
            }else {
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10007;
            }
        }
    }
    cout << dp[n][r] << endl;

}