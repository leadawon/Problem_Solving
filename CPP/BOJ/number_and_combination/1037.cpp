#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
    int num;
    cin >> num;

    int arr[num];

    for (int i=0 ; i< num ; i++){
        cin >> arr[i];
    }

    sort(arr,arr+num);

    if (num % 2 == 1){
        cout << arr[num/2] * arr[num/2] << endl;
    }else{
        cout << arr[0] * arr[num-1] << endl;
    }
}