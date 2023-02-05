#include <iostream>
#include <algorithm>
#include <tuple>
#include <vector>

using namespace std;

bool compare(tuple <long, long> &v1, tuple<long, long> &v2){
    return get<1>(v1) < get<1>(v2);
}

int main(void){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    long n;
    cin >> n;

    long dis[n-1];
    std::vector<tuple <long, long>> co;

    for(long i=0;i<n-1;i++){
        cin >> dis[i];
    }

    int  cost = 0;
    for(long i=0;i<n;i++){
        cin >> cost;

        co.push_back(make_tuple(i,cost));
    }

    sort(co.begin(), co.end(),compare);

    long last_did = n-1;
    long total = 0;

    for(long i =0 ; i<n ; i++){
        if(last_did < get<0>(co[i])){
            continue;
        }

        for(long j=get<0>(co[i]) ; j<last_did ; j++){
            total += dis[j] * get<1>(co[i]);
        }

        last_did = get<0>(co[i]);

        if (last_did == 0){
            break;
        }
    }

    cout << total << endl;



    
    
}