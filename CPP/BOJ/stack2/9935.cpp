#include <iostream>
#include <string>

#include <deque>

using namespace std;

int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);

    deque<char> dq;

    string str1,str2;

    cin >> str1 >> str2;
    
    int counter = str2.size();

    for(int i=0 ; i<str1.size() ; i++){
        dq.push_back(str1[i]);
        if(str1[i] == str2[counter-1]){
            while(counter){
                if(dq.empty() || dq.back() != str2[counter-1]){
                    break;
                }
                dq.pop_back();
                counter--;
            }
            if(counter){
                while(counter < str2.size()){
                    dq.push_back(str2[counter]);
                    counter++;
                }
            }
            counter = str2.size();
        }
    }

    if(dq.empty()){
        cout << "FRULA";
    }else{
        while(!dq.empty()){
            cout << dq.front();
            dq.pop_front();
        }
    }

    return 0;

    

}