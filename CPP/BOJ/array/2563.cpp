#include <iostream>

using namespace std;

int main(void){
    int colpap, row, col;
    cin >> colpap;

    int arr[10][10] = {0};
    for (int i=0; i<colpap; i++){
        cin >> col >> row;
    
        for (int j=row ; j<row+10;j++){
            if (j > 10){
                break;
            }
            for (int k = 0 ; k < col + 10 ; k ++){
                if (k > 10){
                    break;
                }
                arr[j][k] = 1;
            }
        }
    }
    colpap = 0;
    for (int j = 0 ; j < 10 ; j ++){
        for (int k = 0 ; k < 10 ; k ++){
            if (arr[j][k] == 1){
                colpap++;
            }
        }
    }
    cout << colpap << endl;
    
}