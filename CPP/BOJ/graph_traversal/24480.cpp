#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(int a, int b){
    return a > b;
}

void dfs(int visited[],vector<int> map[] , int ans[] , int* ssp, int r){
    for(int i=0 ; i < map[r].size() ; i++){
        if(!visited[map[r][i]]){
            ans[map[r][i]] = *ssp;
            *ssp += 1;
            visited[map[r][i]] = 1;
            dfs(visited , map , ans , ssp , map[r][i]); 
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
        sort(map[i].begin() , map[i].end(), compare);
    }

    int visited[n] = {0,};

    visited[r-1] = 1;

    int ans[n] = {0,};

    ans[r-1] = 1;

    int ss = 2;
    int* ssp = &ss;

    dfs(visited , map , ans , ssp , r-1); 
    

    

    for(int i=0 ; i < n ; i++){
        cout << ans[i] << "\n";
    }

    return 0;
    
}