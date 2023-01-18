#include <iostream>
using namespace std;
int main(void){
    int dot[6];
    for (int i=0;i<6;i++){
        cin >> dot[i];
    }
    if (dot[0] == dot[2]){
        cout << dot[4] << " ";
    }else if(dot[2] == dot[4]){
        cout << dot[0] << " ";
    }else{
        cout << dot[2] << " ";
    }

    if (dot[1] == dot[3]){
        cout << dot[5];
    }else if(dot[3] == dot[5]){
        cout << dot[1];
    }else{
        cout << dot[3];
    }
}