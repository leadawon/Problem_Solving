#include <iostream>
#include <queue>

using namespace std;

struct comp{
    bool operator()(int a, int b){
        int aa,bb;

        if (a < 0){
            aa = -a;
        }else{
            aa = a;
        }

        if (b < 0){
            bb = -b;
        }else{
            bb = b;
        }
        if (aa == bb){
            return a > b;
        }else{
            return aa > bb;
        }

    }
};

int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    priority_queue <int , vector<int>, comp > q;

    int n;
    cin >> n;

    int input;

    for(int i=0 ; i<n ; i++){
        cin >> input;

        if (input == 0){
            if (q.empty()){
                cout << "0" << "\n";
            }else{
                cout << q.top() << "\n";
                q.pop();
            }
        }else{
            q.push(input);
        }
    }

    return 0;
}