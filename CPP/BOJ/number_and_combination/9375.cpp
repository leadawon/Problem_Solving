#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(void){
    map<string, int> m;

    int t,n;

    string str1,str2;
    cin >> t;
    for(int i=0;i<t;i++){
        cin >> n;
        m.clear();
        for (int j=0;j<n;j++){
            cin >> str1 >> str2;
            if (m.find(str2) != m.end()){
                m[str2]++;
            }else{
                m[str2] = 1;
            }
        }
        int suma = 1;
        bool flag = false;
        for (auto iter = m.begin() ; iter !=  m.end(); iter++){
	        suma *= iter->second + 1;
            flag = true;
        }

        if (flag){
            cout<<suma-1<<endl;
        }else{
            cout << 0 << endl;
        }
    }
}