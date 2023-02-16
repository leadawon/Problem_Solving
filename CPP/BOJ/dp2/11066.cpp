#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    int t,k,tmp,suma;
    cin >> t;
    
    int **dp;
    int *arr;
    int *sarr;
    for(int i=0;i<t;i++){
        cin >> k;
        dp = new int*[k+1];
        for(int j=0;j<k+1;j++){
            dp[j] = new int[k+1]();
        }
        arr = new int[k+1]();
        sarr = new int[k+1]();

        for(int j=0 ; j<k ; j++){
            cin >> arr[j+1];
            sarr[j+1] = sarr[j] + arr[j+1];
        }

        for(int j=1 ; j<k ; j++){
            for(int m=1; m<k-j+1;m++){
                //dp[m][m] = arr[m];
                //dp[m+j][m+j] = arr[m+j];

          
                dp[m][m+j] = dp[m][m] + dp[m+1][m+j] + sarr[m+j] - sarr[m-1];
        

                
                for(int n=m;n<m+j;n++){
                    dp[m][m+j] = min(dp[m][m+j], dp[m][n] + dp[n+1][m+j] + sarr[m+j] - sarr[m-1]);
                    //cout << "_____" << dp[m][n] << dp[n+1][m+j] <<"__"<< sarr[m+j] <<"____"<< sarr[m-1] << "\n";
                    //cout << dp[m][m+j] << "\n";
                }
            }
        }

        cout << dp[1][k] << "\n";


        for(int j=0 ; j<k+1 ; j++){
            delete dp[j];
        }
        delete dp;
        delete arr;
        delete sarr;
        


    }

    return 0;
}