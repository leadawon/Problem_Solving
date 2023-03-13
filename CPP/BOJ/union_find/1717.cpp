#include <iostream>

using namespace std;

long find_root(long arr[] , long tg){
    if (arr[tg] == tg){
        return tg;
    }else{
        long tmp = find_root(arr , arr[tg]);
        arr[tg] = tmp;
        return tmp;
    }
}

int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);
    long n,m;
    cin >> n >> m;

    long arr[n+1];
    for(long i = 0 ; i < n+1 ; i++){
        arr[i] = i;
    }
    long cmd[3];

    for(long i = 0 ; i< m ; i++){
        cin >> cmd[0] >> cmd[1] >> cmd[2];
        if (!cmd[0]){
            //union
            if(find_root(arr,cmd[1]) != find_root(arr,cmd[2])){
                arr[find_root(arr,cmd[1])] = cmd[2];
            }
            
        }else{
            //detect
            if(find_root(arr,cmd[1]) == find_root(arr,cmd[2])){
                cout << "YES" << "\n";
            }else{
                cout << "NO" << "\n";
            }
        }
    }
}

/*
0 1 2 3 4 5 6 7
0 7 2 3 4 5 6 7

*/