#include <iostream>
#include <cmath>
using namespace std;
int main(void){
    int T;

    int x1,y1,x2,y2;

    int num;

    cin >> T;

    int ansarr[T];

    for(int testcase = 0 ; testcase < T ; testcase ++ ){
        cin >> x1 >> y1 >> x2 >> y2;

        cin >> num;

        int cx[num];
        int cy[num];
        int r[num];

        for (int planet = 0 ; planet < num ; planet ++){
            cin >> cx[planet] >> cy[planet] >> r[planet];
        }

        int dis_planet_s[num];
        int dis_planet_e[num];

        int answer = 0;

        for (int p=0 ; p<num ; p++){
            dis_planet_s[p] = pow((cx[p] - x1),2) + pow((cy[p] - y1),2);

            dis_planet_e[p] = pow((cx[p] - x2),2) + pow((cy[p] - y2),2);

            if (dis_planet_s[p] > pow(r[p],2)){
                dis_planet_s[p] = 0;
            }else{
                dis_planet_s[p] = 1;
            }

            if (dis_planet_e[p] > pow(r[p],2)){
                dis_planet_e[p] = 0;
            }else{
                dis_planet_e[p] = 1;
            }

            if (dis_planet_s[p] != dis_planet_e[p]){
                answer++;
            }
        }
        ansarr[testcase] = answer;
        
    }
    for(int tc=0;tc<T;tc++){
        cout << ansarr[tc] << endl;
    }
}