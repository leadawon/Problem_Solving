#include <iostream>
#include <queue>
using namespace std;

int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);
    priority_queue<long , vector<long>> q;

    long n;
    long input;

    cin >> n;

    for(int i=0 ; i<n; i++){
        cin >> input;

        if (input){
            q.push(input);
        }else{
            if (q.empty()){
                cout << "0" << "\n";
            }else{
                cout << q.top() << "\n";
                q.pop();
            }
        }

        
    }

}