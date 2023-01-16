#include <iostream>

using namespace std;

int main(){
    int num;
    cin >> num;
    int cnt[num];
    for (int i = 0 ; i < num ; i ++){
        cin >> cnt[i];
    }
    int temp;
    cin >> temp;

    int ans=0;
    for (int i = 0 ; i < num ; i ++){
        if (cnt[i] == temp){
            ans++;
        }
    }
    cout << ans << endl;




}