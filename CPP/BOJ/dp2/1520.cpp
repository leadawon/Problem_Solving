#include <iostream>
#include <queue>
using namespace std;

struct tup{
    int row,col;
    long value;
};
typedef tup tup;


struct comp{
    bool operator()(tup &a, tup &b){
        return a.value < b.value;

    }
};


int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    int m,n;

    cin >> m >> n;

    priority_queue <tup , vector<tup>, comp> q;

    int** arr = new int*[m];
    long** dp = new long*[m];


    for(int i=0;i<m;i++){
        arr[i] = new int[n]();
        dp[i] = new long[n]();
    }

    int tmp;
    tup T_O;

    for(int i=0 ; i<m ; i++){
        for(int j=0 ; j<n ;j++){
            cin >> tmp;
            arr[i][j] = tmp;

            T_O.row = i;
            T_O.col = j;
            T_O.value = tmp;

            q.push(T_O);
        }
    }

    dp[0][0] = 1;

    for(int i=0 ; i<m ; i++){
        for(int j=0 ; j<n ;j++){
            T_O = q.top(); q.pop();

            if (T_O.row > 0){//상
                if(arr[T_O.row][T_O.col] < arr[T_O.row-1][T_O.col]){
                    dp[T_O.row][T_O.col] += dp[T_O.row-1][T_O.col];
                }
            }
            if (T_O.col < n-1){//우
                if(arr[T_O.row][T_O.col] < arr[T_O.row][T_O.col+1]){
                    dp[T_O.row][T_O.col] += dp[T_O.row][T_O.col+1];
                }
            }
            if (T_O.row < m-1){//하
                if(arr[T_O.row][T_O.col] < arr[T_O.row+1][T_O.col]){
                    dp[T_O.row][T_O.col] += dp[T_O.row+1][T_O.col];
                }
            }
            if(T_O.col > 0){//좌
                if(arr[T_O.row][T_O.col] < arr[T_O.row][T_O.col-1]){
                    dp[T_O.row][T_O.col] += dp[T_O.row][T_O.col-1];
                }
            }

        }
    }

    cout << dp[m-1][n-1] << endl;


}