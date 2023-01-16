#include <iostream>

using namespace std;

int main(void){
    int input, row, col;
    int maxval = -1;
    for (int i=1 ; i<10 ; i++){
        for (int j=1 ; j<10 ; j++){
            cin >> input;
            if (input > maxval){
                maxval = input;
                row = i;
                col = j;
            }
        }
    }
    cout << maxval << endl << row << " " << col;
}