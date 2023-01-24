#include <iostream>

using namespace std;

int gcd(int a, int b)
{
	int c;
	while (b != 0)
	{
		c = a % b;
		a = b;
		b = c;
	}
	return a;
}

int lcm(int a, int b)
{
    return a * b / gcd(a, b);
}

int main(void){
    int num;
    cin >> num;

    int r[num];

    int lcm_num;

    for (int i=0;i<num;i++){
        cin >> r[i];
        if (i!=0){
            lcm_num = lcm(r[0],r[i]);
            cout << lcm_num / r[i] << "/" << lcm_num / r[0] << endl;
        }
    }
}