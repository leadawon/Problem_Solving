#include <iostream>
#include <map>

using namespace std;

int main(void){
    map<int,bool> map_a , map_b;
    int num_a , num_b;

    cin >> num_a >> num_b;

    int temp;
    for (int i=0;i<num_a;i++){
        cin >> temp;
        map_a[temp] = 1;
    }
    for (int i=0;i<num_b;i++){
        cin >> temp;
        map_b[temp] = 1; 
    }
    int cnt = 0;
    for (auto iter = map_a.begin() ; iter != map_a.end();iter++){
        if (map_b[iter->first] == 0){
            cnt++;
        }
    }

    for (auto iter = map_b.begin() ; iter != map_b.end() ; iter++){
        if (map_a[iter->first] == 0){
            cnt++;
            
        }
        
    }
    cout << cnt << endl;

}