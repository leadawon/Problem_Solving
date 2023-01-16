#include <iostream>
using namespace std;
int main(void){
    int row,col;
    cin >> row >> col;

    int matrix1[row][col];
    for (int i = 0 ; i < row; i++){
        for (int j = 0 ; j < col; j++){
            cin >> matrix1[i][j];
        }
    }

    int matrix2[row][col];
    for (int i = 0 ; i < row; i++){
        for (int j = 0 ; j < col; j++){
            cin >> matrix2[i][j];
            matrix1[i][j] += matrix2[i][j];
        }
    }

    for (int i = 0 ; i < row; i++){
        for (int j = 0 ; j < col; j++){
            cout << matrix1[i][j] << " ";
        }
        cout << endl;
    }

}