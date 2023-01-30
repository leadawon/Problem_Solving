#include <iostream>

using namespace std;

void dfs(int depth, int arr[] , int n, int r){
    if (depth == r){
        for(int i=0 ; i< r ; i++){
            cout << arr[i] << " ";
        }
        cout << "\n";
        return;
    }

    for(int i=1;i<=n;i++){
        if(depth==0 || arr[depth-1] <= i){
            arr[depth] = i;
            dfs(depth+1, arr, n , r);
        }
    }
}

int main(void){
    int n,r;
    int arr[n] = {0};

    cin >> n >> r;
    dfs(0,arr,n,r);
}