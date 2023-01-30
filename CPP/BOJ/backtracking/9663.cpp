#include <iostream>

using namespace std;




//퀸 배치하고 이동가능 경로 1로 색칠하는 함수
void queen_1(int row, int col, int** arr, int n){
    // 가로줄
    for(int i=0;i<n;i++){
        arr[row][i] += 1;
    }
    // 세로줄
    for(int i=0;i<n;i++){
        arr[i][col] += 1;
    }

    // 좌상 -> 우하
    if (row > col){
        for(int i=0;row-col+i<n;i++){
            arr[row-col+i][i] += 1;
        }
    }
    else{ // row <= col
        for(int i=0;col-row+i<n;i++){
            arr[i][col-row+i] += 1;
        }

    }

    // 우상 -> 좌하
    if (row+col > n-1){
        for(int i=row+col-(n-1); i<n;i++){
            arr[i][row+col-i] += 1;
        }
    }else{
        for(int i=0; i<row+col+1;i++){
            arr[i][row+col-i] += 1;
        }
    }

    return;
    

}

void queen_0(int row, int col, int** arr, int n){
    // 가로줄
    for(int i=0;i<n;i++){
        arr[row][i] -= 1;
    }
    // 세로줄
    for(int i=0;i<n;i++){
        arr[i][col] -= 1;
    }

    // 좌상 -> 우하
    if (row > col){
        for(int i=0;row-col+i<n;i++){
            arr[row-col+i][i] -= 1;
        }
    }
    else{ // row <= col
        for(int i=0;col-row+i<n;i++){
            arr[i][col-row+i] -= 1;
        }

    }

    // 우상 -> 좌하
    if (row+col > n-1){
        for(int i=row+col-(n-1); i<n;i++){
            arr[i][row+col-i] -= 1;
        }
    }else{
        for(int i=0; i<row+col+1;i++){
            arr[i][row+col-i] -= 1;
        }
    }

    return;
    

}

//depth가 n-1에 도달했을때 배치가능한 자리의 갯수 카운트
//아직 도달 안했을때는 색칠하면서 dfs한다.
void dfs(int depth ,int** arr ,int n, int* ptr){
    if(depth == n-1){
        for(int j=0 ; j< n ; j++){
            if(arr[depth][j] == 0){
                *ptr += 1;
            }
        }
        return;
    }



    for(int j=0;j<n;j++){
        if (arr[depth][j] == 0){
            queen_1(depth, j, arr, n);
            dfs(depth+1,arr,n,ptr);
            queen_0(depth, j, arr, n);
        }
    }


    
}

int main(void){
    int n, cnt;
    cnt=0;
    cin >> n;
    int** arr = new int*[n];
    for(int i=0;i<n;i++){
        arr[i] = new int[n];
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            arr[i][j] = 0;
        }

    }

    dfs(0,arr,n,&cnt);

    cout << cnt << endl;

    for(int i=0;i<n;i++){
        delete[] arr[i];
    }
    delete[] arr;
}
