#include <iostream>
#include <string>
#include <typeinfo>
using namespace std;
int main(void){

    string str;
    getline(cin, str);
    int n1 = std::stoi(str);
    getline(cin, str);
    int n2 = std::stoi(str);
    
    cout << n1 * n2 << endl;
    return 0;
}
