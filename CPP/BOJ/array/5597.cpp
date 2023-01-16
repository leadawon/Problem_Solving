#include <iostream>
using namespace std;
int main(void){
    int arr[31] = {0};
    arr[0] = 1;
    int input;
    for (int i=0 ; i<28 ; i++){
        cin >> input;
        arr[input] = 1;   
    }

    for (int i=0 ; i<31 ; i++){
        if (arr[i] == 0){
            cout << i << endl;
        }
        
    }
    return 0;
}