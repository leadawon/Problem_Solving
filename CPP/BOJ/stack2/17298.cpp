#include <iostream>
#include <queue>
using namespace std;


struct tp{
    long index;
    long value;
};

struct comp{
    bool operator()(tp &a , tp &b){
        return a.value > b.value;
    }
};

int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    priority_queue<tp, vector<tp>, comp> pq;

    long n, tmp;

    cin >> n;

    long arr[n] = {0,};
    long ans[n];

    for(int i=0 ; i<n ; i++){
        ans[i] = -1;
    }

    tp tmp_tp;

    for(int i=0 ; i<n; i++){
        cin >> arr[i];
        tmp_tp.index = i;
        tmp_tp.value = arr[i];
        pq.push(tmp_tp);

        while (!pq.empty() && pq.top().value < arr[i]){
            ans[pq.top().index] = arr[i];
            pq.pop();
        }
    }

    for(int i=0 ; i<n ; i++){
        cout << ans[i] << " ";
    }



    return 0;


}