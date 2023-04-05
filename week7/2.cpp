#include <iostream> 
using namespace std; 
 
void print_numbers(int n) { 
    if (n == 0) {  
        return; 
    } 
 
    print_numbers(n/10);  
    cout << n%10 << " ";  
} 
 
int main() { 
    int n; 
    cin >> n; 
 
    print_numbers(n); 
    return 0; 
}