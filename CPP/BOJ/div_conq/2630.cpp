#include <iostream>

using namespace std;

void dfs(int** arr, int pos[],  int* ptr0 ,int* ptr1 , int len){

    int base = arr[pos[0]][pos[1]];

    bool flag = false;

    for(int i=pos[0] ; i < len+pos[0] ; i++){
        for(int j=pos[1] ; j < len+pos[1] ; j++){
            if (base != arr[i][j]){
                flag = true;
                break;
            }
        }
    }
    



    if (flag){
        int sub_pos[2];

        sub_pos[0] = pos[0];
        sub_pos[1] = pos[1];

        dfs(arr, sub_pos, ptr0,ptr1, (int)len/2);

        sub_pos[0] = pos[0];
        sub_pos[1] = pos[1] + (int)len/2;


        dfs(arr , sub_pos,ptr0,ptr1,(int)len/2);

        sub_pos[0] = pos[0] + (int)len/2;
        sub_pos[1] = pos[1];

        dfs(arr , sub_pos,ptr0,ptr1,(int)len/2);
        
        sub_pos[0] = pos[0] + (int)len/2;
        sub_pos[1] = pos[1] + (int)len/2;

        dfs(arr , sub_pos,ptr0,ptr1,(int)len/2);

    }else{
        if(base){
            *ptr1 += 1;
        }else{
            *ptr0 += 1;
        }
    }
}


int main(void){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int n;
    int cnt0 = 0;
    int cnt1 = 0;

    cin >> n;

    int** arr = new int*[n];



    for(int i=0;i<n;i++){
        arr[i] = new int[n];
    } 


    int pos[2];

    pos[0] = 0; 
    pos[1] = 0;


    

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin >> arr[i][j];
        }
    }

    dfs(arr, pos, &cnt0,&cnt1, n);

    cout << cnt0 << "\n" << cnt1 << endl;



}