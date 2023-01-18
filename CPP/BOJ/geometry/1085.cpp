#include <iostream>
using namespace std;
int main(void){
    int qd[4];
    int leng[4];

    cin >> qd[0] >> qd[1] >> qd[2] >> qd[3];

    leng[0] = qd[0];
    leng[1] = qd[1];
    leng[2] = qd[2] - qd[0];
    leng[3] = qd[3] - qd[1];

    for(int i = 0 ; i < 4 ; i ++ ){
        if (leng[0] > leng[i]){
            leng[0] = leng[i];
        }
    }

    cout << leng[0] << endl;

}