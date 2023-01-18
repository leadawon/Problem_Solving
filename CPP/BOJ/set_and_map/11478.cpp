#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

int main(void){
    unordered_set<string> s;
    string str;

    string tempstr;

    getline(cin , str);
    for(int i = 1 ; i < str.size() + 1 ; i++){
        for(int j = 0 ; j < str.size() + 1 - i ; j++){
            tempstr.clear();
            for(int k = j ; k < j+i ; k++){
                tempstr += str[k];

            }
            s.insert(tempstr);
            
        }
        
    }

    cout << s.size() << endl;
    
}