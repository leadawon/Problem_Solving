#include <iostream>

using namespace std;

void nine(int** arr , int pos[] , int len, int cnt[]){
    int base = arr[pos[0]][pos[1]];

    bool flag = false;

    for(int i=pos[0]; i<pos[0]+len;i++){
        for(int j=pos[1];j<pos[1]+len;j++){
            if(base != arr[i][j]){
                flag = true;
                break;
            }
        }
        if(flag)
            break;
    }

    if(flag){
        int sub_pos[2];
        sub_pos[0] = pos[0];
        sub_pos[1] = pos[1];

        nine(arr,sub_pos,len/3,cnt);

        sub_pos[0] = pos[0];
        sub_pos[1] = pos[1] + len/3;

        nine(arr,sub_pos,len/3,cnt);

        sub_pos[0] = pos[0];
        sub_pos[1] = pos[1] + len/3 + len/3;

        nine(arr,sub_pos,len/3,cnt);

        sub_pos[0] = pos[0] + len/3;
        sub_pos[1] = pos[1];

        nine(arr,sub_pos,len/3,cnt);

        sub_pos[0] = pos[0] + len/3;
        sub_pos[1] = pos[1] + len/3;

        nine(arr,sub_pos,len/3,cnt);

        sub_pos[0] = pos[0] + len/3;
        sub_pos[1] = pos[1] + len/3 + len/3;

        nine(arr,sub_pos,len/3,cnt);

        sub_pos[0] = pos[0] + len/3 + len/3;
        sub_pos[1] = pos[1];

        nine(arr,sub_pos,len/3,cnt);

        sub_pos[0] = pos[0] + len/3 + len/3;
        sub_pos[1] = pos[1] + len/3;

        nine(arr,sub_pos,len/3,cnt);

        sub_pos[0] = pos[0] + len/3 + len/3;
        sub_pos[1] = pos[1] + len/3 + len/3;

        nine(arr,sub_pos,len/3,cnt);
    }else{
        if(base==-1){
            cnt[0]++;
        }else if(base==0){
            cnt[1]++;
        }else{
            cnt[2]++;
        }
    }
}


int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    int n;
    cin >> n;

    int** arr = new int*[n];

    for(int i=0;i<n;i++){
        arr[i] = new int[n];
        for(int j=0;j<n;j++){
            
            cin >> arr[i][j];
        }
    }

    int pos[2];
    pos[0] = 0;
    pos[1] = 0;

    int cnt[3] = {0,};

    nine(arr,pos,n ,cnt);
    cout << cnt[0] << "\n" << cnt[1] << "\n" << cnt[2] << endl;
}