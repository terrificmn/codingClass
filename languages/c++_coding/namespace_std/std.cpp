#include <iostream>
using std::cout;
using std::endl;
using std::string;
using std::abs;
//using namespace std;

namespace namespace25 {
    int age = 25;
    string name = "Tim";
}

namespace namespace30 {
    int age = 30;
}

// int abs(int number) {
// 	return number + 5;
// }


int main() {
    
    cout << namespace25::age << endl;
    cout << namespace25::name << endl;

}