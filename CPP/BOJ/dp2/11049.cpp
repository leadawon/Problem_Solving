#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    int n,tmp;
    cin >> n;

    long** dp = new long*[n+1];
    long** arr = new long*[n+1];

    for(long i=0;i<n+1 ; i++){
        dp[i] = new long[n+1]();
        arr[i] = new long[2]();

    }

    for(long i=1 ; i<n+1 ; i++){
        cin >> arr[i][0];
        cin >> arr[i][1];
    }

    for(int i=1;i<n;i++){
        for(int j=1 ; j<n-i+1; j++){
            dp[j][j+i] = dp[j][j] + dp[j+1][j+i] + arr[j][0] * arr[j][1] * arr[j+i][1];
            for(int k=j ; k<j+i;k++){
                dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + arr[j][0] * arr[k][1] * arr[j+i][1]);
            }
        }
    }

    cout << dp[1][n];

    for(int i=0;i<n+1;i++){
        delete dp[i];
        delete arr[i];
    }

    delete dp;
    delete arr;

    return 0;
}