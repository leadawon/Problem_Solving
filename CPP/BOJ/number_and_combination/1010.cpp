#include <iostream>

using namespace std;

int main(void){
    int t;
    cin >> t;
    int tg[t][2];

    int maxnum0=0;
    int maxnum1=0;

    for(int i=0;i<t;i++){
        cin >> tg[i][0] >> tg[i][1];
        if (tg[i][0]>maxnum0){
            maxnum0 = tg[i][0];
        }
        if(tg[i][1] > maxnum1){
            maxnum1 = tg[i][1];
        }
    }

    int dp[maxnum1+1][maxnum0+1];

    dp[0][0] = 1;
    dp[1][0] = 1;
    dp[1][1] = 1;
    for(int i =2 ; i<=maxnum1;i++){
        for(int j=0;j<=i;j++){
            if (j == 0) {
                dp[i][0] = 1;
            }else if (j == i) {
                dp[i][j] = 1;
            }else {
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            }
            if (j == maxnum0){
                break;
            }
        }
    }
    for(int i =0 ;i<t;i++){
        cout << dp[tg[i][1]][tg[i][0]] << endl;
    }
}