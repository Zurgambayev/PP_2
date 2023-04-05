#include <iostream> 
#include <vector>
using namespace std; 
 
int main(){ 
    int n,m; 
    cin>>n>>m; 
    vector <int> vt(n);
    vector <int> v(m);
    for(int i=0;i<n;i++){ 
        cin>>vt[i]; 
    } for(int i=0;i<m;i++){ 
        cin>>v[i]; 
    } 
    int cnt = 0;
    for (int i = 0; i < v.size();i++){
        for (int j = 0; j < vt.size();j++){
            if(v[i] == vt[j]){
                cnt++;
            }
        }
        if (cnt == 0){
            cout << "NO" << endl ;
        }else {
            cout << "YES" << endl;
            cnt = 0;
        }
    }
}