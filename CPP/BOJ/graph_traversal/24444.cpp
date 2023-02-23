#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

void bfs(int visited[] , vector<int> map[] , int r , int ans[] , int* ssp, deque<int> dq){


    dq.push_back(r);

    while(!dq.empty()){
        int x = dq.front();

        dq.pop_front();

        ans[x] = *ssp;
        *ssp += 1;

        for(int i =0 ; i<map[x].size(); i++){
        if(!visited[map[x][i]]){
            dq.push_back(map[x][i]);
            visited[map[x][i]] = 1;
        }


    }

    }

    
}


int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    int n,m,r,u,v;

    cin >> n >> m >> r;

    vector<int> map[n];

    for(int i=0 ; i<m ; i++){
        cin >> u >> v;

        map[u-1].push_back(v-1);
        map[v-1].push_back(u-1);

    }

    for(int i=0 ; i<n ; i++){
        sort(map[i].begin() , map[i].end());
    }

    int ans[n] = {0,};


    int ss = 1;
    int* ssp = &ss;

    int visited[n] = {0,};
    visited [r-1] = 1;

    deque<int> dq;


    bfs(visited , map , r-1 , ans, ssp , dq);

    for(int i=0 ; i< n ; i++){
        cout << ans[i] << "\n";
    }

}