#include <iostream>

using namespace std;

int main(void){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    const int a_ASCII = 97;

    string str;
    cin >> str;

    int q;
    cin >> q;

    char tg;
    int l,r;

    int size_of_str = str.size();

    int arr[26][size_of_str];

    for(int i=0 ; i<26;i++){
        for(int j=0 ; j<size_of_str ; j++){
            arr[i][j] = 0;
        }
    }

    int max_searched = 0;

    arr[(int)str[0] - a_ASCII][0] = 1;

    for(int i=0 ; i<q; i++){
        cin >> tg >> l >> r;

        if (r > max_searched){
            for(int j = max_searched + 1 ; j < r+1 ; j++){
                for(int k = 0 ; k<26 ; k++){
                    if (k == (int)str[j]-a_ASCII){
                        arr[k][j] = arr[k][j-1] + 1;
                    }else{
                        arr[k][j] = arr[k][j-1];
                    }
                }
            }
            max_searched = r;
        }

        if(l > 0){
            cout << arr[(int)tg - a_ASCII][r] - arr[(int)tg-a_ASCII][l-1] << '\n';
        }else{
            cout << arr[(int)tg - a_ASCII][r] << '\n';
        }

    }
}