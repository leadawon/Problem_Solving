#include <iostream>
#include <vector>
using namespace std;

template<typename T>

void pop_front(vector<T> &v)
{
    if (v.size() > 0) {
        v.erase(v.begin());
    }
}


int small_to_big(int s){
    if (s==0){
        return 1;
    }else if(s==1){
        return 0;
    }else if(s==2){
        return 3;
    }else{
        return 2;
    }
}

int main(void){
    int ym;
    cin >> ym;

    vector<int> field[4];
    vector<int> seq;
    int index, length;



    for (int i=0; i<6 ; i++){
        cin >> index >> length;

        field[index-1].push_back(length);
        seq.push_back(index-1);
    }

    vector<int> curve;
    for (int i=0;i<4;i++){
        if(field[i].size() == 2){
            curve.push_back(i);
        } 
    }

    int temp;
    for (int i=0;i<4;i++){
        if(seq[0] == curve[0]){
            pop_front(seq);
            seq.push_back(curve[0]);
            temp=field[curve[0]][0];
            field[curve[0]][0] = field[curve[0]][1];
            field[curve[0]][1] = temp;
        }else if(seq[0] == curve[1]){
            pop_front(seq);
            seq.push_back(curve[1]);
            temp=field[curve[1]][0];
            field[curve[1]][0] = field[curve[1]][1];
            field[curve[1]][1] = temp;
        }else{
            break;
        }
    }


    int small_1, small_2;
    for (int i=0;i<6;i++){
        if (curve[0] == seq[i]){
            small_1 = field[curve[0]][1];
            small_2 = field[curve[1]][0];
            break;
        }else if(curve[1] == seq[i]){
            small_1 = field[curve[1]][1];
            small_2 = field[curve[0]][0];
            break;
        }
    }
    
    int big_1 = field[small_to_big(curve[0])][0];
    int big_2 = field[small_to_big(curve[1])][0];

    int answer = (big_1 * big_2 - small_1 * small_2) * ym;
    cout << answer << endl;
    

}