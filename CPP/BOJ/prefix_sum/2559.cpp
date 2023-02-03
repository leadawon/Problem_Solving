#include <iostream>
using namespace std;
int main(void){
    int n,k;
    
    long max;
    long sum=0;


    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> n >> k;
    long arr[k] = {0,};
    max = (long)(-100 * k);

    for(int i=0; i<n;i++){
        
        sum -= arr[i%k];

        cin >> arr[i%k];

        sum += arr[i%k];

        if (sum > max && i >= k-1){
            max = sum;
        }


    }

    cout << max;


}