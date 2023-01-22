#include <iostream>

using namespace std;

int main(void){
    int f,l;
    while(true){
        cin >> f >> l;
        if (f==0 && l==0){
            break;
        }
        if (f % l == 0){
            cout << "multiple" << endl;
        }
        else if (l % f == 0){
            cout << "factor" << endl;
        }else{
            cout << "neither" << endl;
        }

    }
}