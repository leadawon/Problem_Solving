#include <iostream>
#include <cmath>
using namespace std;
int main(void){
    int trian[3];
    int max_len = 0;
    int rest_idx[2];
    while(true){
        cin >> trian[0] >> trian[1] >> trian[2];
        max_len = 0;
        if (trian[0] > max_len){
            max_len = trian[0];
            rest_idx[0] = 1;
            rest_idx[1] = 2;
        }
        if (trian[1] > max_len){
            max_len = trian[1];
            rest_idx[0] = 0;
            rest_idx[1] = 2;
        }
        if (trian[2] > max_len){
            max_len = trian[2];
            rest_idx[0] = 1;
            rest_idx[1] = 0;
        }

        if(max_len == 0){
            break;
        }

        if (pow(max_len,2) == pow(trian[rest_idx[0]], 2) + pow(trian[rest_idx[1]],2)){
            cout << "right" << endl;
        }else{
            cout << "wrong" << endl;
        }

    }
}