#include <iostream>

using namespace std;

int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    long k,n;
    cin >> k >> n;
    long arr[k]={0,};

    long maxnum = 0;
    long tmp = 0;

    for(long i=0;i<k;i++){
        cin >> tmp;
        arr[i]=tmp;
        if (tmp > maxnum){
            maxnum = tmp;
        }
    }

    long minnum = 0;
    long suma = 0;

    while(1){
        tmp = (maxnum + minnum)/2;
        if (!tmp){
            minnum+=1;
            continue;
        }
        suma = 0;
        for(int i=0;i<k;i++){
            suma+=(arr[i]/tmp);
        }
        if (suma>=n){
            if(maxnum == minnum){
                break;
            }else if(maxnum == minnum + 1){
                suma = 0;
                for(int i=0;i<k;i++){
                    suma+=(arr[i]/(tmp+1));
                }
                if (suma >= n){
                    tmp += 1;
                }
                break;
            }else{
                minnum = tmp;
            }
        }else{
            maxnum = tmp-1;

        }

    }
    cout << tmp;





    

}