#include <iostream>

using namespace std;

int main(void){
    ios::sync_with_stdio; cin.tie(NULL); cout.tie(NULL);
    int n,m;    

    cin >> n >> m;

    int** m1 = new int*[n];

    for(int i=0; i<n;i++){
        m1[i] = new int[m];
    }

    for(int i=0 ; i<n; i++){
        for(int j=0 ; j<m; j++){
            cin >> m1[i][j];
        }
        
    }

    int k;

    cin >> m >> k;

    int **m2 = new int*[m];

    for(int i=0; i<m;i++){
        m2[i] = new int[k];
    }

    for(int i=0 ; i<m ; i++){
        for(int j=0 ;j<k ; j++){
            cin >> m2[i][j];
        }
    }

    int **m3 = new int*[n];
    for(int i=0; i<n;i++){
        m3[i] = new int[k];
        for(int j=0 ; j<k;j++){
            m3[i][j] = 0;
        }
    }


    for(int i=0;i<n;i++){
        for(int j=0;j<k;j++){
            for(int p = 0 ; p < m ; p++){
                m3[i][j] += m1[i][p] * m2[p][j];
            }
            cout << m3[i][j] << " ";
        }
        cout << "\n";
    }

}