#include <iostream>

using namespace std;

int main(void){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int n,m;
    cin >> n >> m;

    int arr[n];

    int s,e;

    long sum[n];

    for(int i = 0; i < n; i++){
        sum[i] = 0;
    }

    for(int i = 0; i < n ; i++){
        cin >> arr[i];
    }

    sum[0] = arr[0];

    for(int i=1 ; i<n ; i++){
        sum[i] += sum[i-1] + arr[i];
    }

    for(int i=0;i<m;i++){
        cin >> s >> e;
        s -= 1;
        e -= 1;
        
        
        if (s==0){
            cout << sum[e] << "\n";
        }else{
            cout << sum[e] - sum[s-1] << "\n";
        }
        
    }
}