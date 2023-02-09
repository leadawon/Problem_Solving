#include <iostream>

using namespace std;

long long dfs(long long a ,long long b ,long long c){
    if (b==1){
        return a%c; 
    }else if(b % 2 == 0 ){
        long long d = dfs(a,b/2,c);
        return (d*d) % c;
    }else{
        long long d = dfs(a,(b-1)/2 , c);
        return ((d * d)%c * a) %c;
    }
} 

int main(void){
    ios::sync_with_stdio;cin.tie(NULL);cout.tie(NULL);

    long long a,b,c;
    cin >> a >> b >> c;

    
    cout << dfs(a,b,c);

}