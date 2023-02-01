#include <iostream>

using namespace std;

long max(long a , long b , long c=0){
    if (a >= b && a >= c){
        return a;
    }else if(b >= a && b >= c){
        return b;
    }else{
        return c;
    }
}

int main(void){
    int n;
    
    cin >> n;

    int wine[n];

    int ml;

    for(int i=0;i<n;i++){
        cin >> ml;
        wine[i] = ml;
    }

    long dp[n+3][3]; // v  x  w

    for(int i=0 ; i<n ; i++){
        dp[i][0] = 0;
        dp[i][1] = 0;
        dp[i][2] = 0;
    }

    dp[0][0] = wine[0];
    dp[0][1] = 0;
    dp[0][2] = 0;

    dp[1][0] = wine[1];
    dp[1][1] = dp[0][0] + wine[1];
    dp[1][2] = 0;

    dp[2][0] = max(dp[0][0], dp[0][1]) + wine[2];
    dp[2][1] = dp[1][0] + wine[2];
    dp[2][2] = 0;

    dp[3][0] = max(dp[1][0] , dp[1][1]) + wine[3];
    dp[3][1] = max(dp[2][0] , dp[0][2]) + wine[3];
    dp[3][2] = 0;

    for(int i=4;i<n;i++){
        dp[i][0] = max(dp[i-2][0] , dp[i-2][1]) + wine[i];
        dp[i][1] = max(dp[i-1][0] , dp[i-1][2]) + wine[i];
        dp[i][2] = dp[i-3][1] + wine[i];
    }

    if (n > 1){
        cout << max(max(dp[n-1][0],dp[n-1][1],dp[n-1][2]), max(dp[n-2][0], dp[n-2][1], dp[n-2][2])) << endl;
    }else{
        cout << max(dp[n-1][0],dp[n-1][1],dp[n-1][2])<< endl;
    }







}