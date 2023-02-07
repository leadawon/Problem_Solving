#include <iostream>

using namespace std;

void qt(int** arr, int pos[], int len){
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
        cout << "(";
        int sub_pos[2];
        sub_pos[0] = pos[0];
        sub_pos[1] = pos[1];

        qt(arr , sub_pos, len/2);

        sub_pos[0] = pos[0];
        sub_pos[1] = pos[1] + len/2;

        qt(arr , sub_pos , len/2);

        sub_pos[0] = pos[0] + len/2;
        sub_pos[1] = pos[1];

        qt(arr, sub_pos,len/2);

        sub_pos[0] = pos[0] + len/2;
        sub_pos[1] = pos[1] + len/2;

        qt(arr, sub_pos, len/2);
        cout << ")";
    }else{
        cout << base;
    }
    
}

int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    int n;
    cin >> n;

    int **arr = new int*[n];

    for(int i=0 ;i <n;i++){
        arr[i] = new int[n];
    }

    int pos[2];
    pos[0] = 0;
    pos[1] = 0;

    int row=0;
    for(int i=0;i<n;i++){

        for(int j=0 ; j<n;j++){
            arr[i][j]=((int)cin.get()) - 48;
            if (arr[i][j] == -38){
                arr[i][j]=((int)cin.get()) - 48;
            }
            
        }   
    }
    qt(arr,pos,n);


}