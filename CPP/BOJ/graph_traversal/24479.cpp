#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void dfs(int visited[], vector<int> map[] , int r, int ans[] , int* ss){
    for(int i=0 ; i<map[r].size(); i++){
        if (visited[map[r][i]] == 0){
            visited[map[r][i]] = 1;
            ans[map[r][i]] = *ss;

            *ss += 1;

            dfs(visited, map, map[r][i] , ans, ss);
        }

    }
}

int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    int n,m,r,u,v;

    cin >> n >> m >> r;

    vector<int> map[n];
    

    int* visited = new int[n]();

    visited[r-1] = 1;

    for(int i=0 ; i<m ; i++){
        
        cin >> u >> v;

        map[u-1].push_back(v-1);
        map[v-1].push_back(u-1);
       
    }

    for(int i=0 ; i < n ; i ++ ){
        sort(map[i].begin(), map[i].end());
    }



    int* ans = new int[n]();


    int ssv=1;
    int* ss = &ssv;

    ans[r-1] = *ss;

    *ss += 1;

    dfs(visited , map , r-1, ans,ss);


    for(int i=0 ; i< n ; i++){
        cout << ans[i] << "\n";
    }
    delete visited;
    delete ans;

}