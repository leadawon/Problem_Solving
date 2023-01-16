#include <iostream>

using namespace std;

int main(void){
    int colpap, row, col;
    cin >> colpap;

    int arr[100][100] = {0};
    for (int i=0; i<colpap; i++){
        cin >> row >> col;
    
        for (int j=row ; j<row+10;j++){
            if (j >= 100){
                break;
            }
            for (int k = col ; k < col + 10 ; k ++){
                if (k >= 100){
                    break;
                }
                arr[j][k] = 1;
            }
        }
    }
    colpap = 0;
    for (int j = 0 ; j < 100; j ++){
        for (int k = 0 ; k < 100 ; k ++){
            if (arr[j][k] == 1){
                colpap++;
            }
        }
    }
    cout << colpap << endl;
    
}