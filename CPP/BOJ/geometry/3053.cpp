#include <iostream>
#include <math.h>

using namespace std;

int main(void){
    
    double r;
    cin >> r;
    cout << fixed;
    cout.precision(6);
    cout << r*r*M_PI << "\n" << r*r*2;
}