#include <iostream>

using namespace std;

void dfs(int depth, int arr[] ,bool visited[] , int n, int r)
{
    if(depth == r)
    {
        for(int i = 0; i < r; i++)
            cout << arr[i] << ' ';
        cout << "\n";
        return;
    }
    for(int i = 1; i <= n; i++)
    {
        if(!visited[i])
        {
            visited[i] = true;
            arr[depth] = i;
            dfs(depth+1 , arr, visited , n , r);
            visited[i] = false;
        }
    }
}

int main() {
    int n,r;
    int arr[n] = {0};
    bool visited[n] = {false};
    cin >> n >> r;
    dfs(0, arr , visited , n ,r);
}