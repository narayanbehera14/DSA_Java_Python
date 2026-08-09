// #include<iostream>
// using namespace std;
// int main() {
//     int n = 3; 
//     for (int i = 1; i<=n; i++){
//         for (int j = 1; j<=2; j++){
//             cout << j;
//         }
//         cout << endl;
//     }
//     return 0 ;

// }
// #include <iostream>
// #include <list>
// using namespace std;

// int main(){
//     list<string> cars = {"volvo","BMW","ford","mazda"};
//     cars.front() = "opel";

//     cars.back() = "toyota";

//     cout << cars.front() <<"\n" ;
//     cout << cars.back() <<"\n";
//     cout << "cars"  << cars<< endl;
//     return  0 ;
// }

// #include <iostream>
// #include <list>
// using namespace std ;

// int main () {
//     list<string> cars = {"volvo","BMW","ford","mazda"};
//     cars.push_front("Tesla");
//     cars.push_back("Maruti");
//     for(string car : cars) {
//         cout << car << "\n";
//     }
//     return 0;
// }

// #include <iostream>
// #include <list>
// using namespace std;

// int main() {
//     list<string> cars = {"volvo","BMW","ford","mazda"};
//     cars.pop_front();
//     cars.pop_back();

//     for (string car : cars){
//         cout << car << "\n";
//     }
//     return 0;
// }


// #include <iostream>
// #include<list>
// using namespace std;

// int main() {
//     list<string> cars;
//     cout << cars.empty();
//     return 0;
// }

// #include<iostream>
// #include<list>
// using namespace std ;
// int main(){
//     list<string> cars = {"volvo","bmw","ford","mazda"};
//     for(string car : cars) {
//         cout << car << "\n";
//     }
//     return 0;
// }

// #include <iostream>
// #include<stack>
// using namespace std;
// int main() {
//     stack<string> cars;
//     cars.push("volvo");
//     cars.push("bmw");
//     cars.push("lambo");

//     cout << cars.top() << endl;
//     return 0;
// }

// #include<iostream>
// #include<stack>
// using namespace std;
// int main() {
//     stack<string> cars;
//     cars.push("liju");
//     cars.push("dev");
//     cars.push("behera");

//     cout << cars.top() << endl;
//     return 0;
// }

#include<iostream>
#include<stack>
using namespace std;

int main(){
    stack<string> cars ;
    cars.push("bmw");
    cars.push("volvo");
    cars.push("lambo");
    cars.push("maruti");

    cars.top()= "tarzan";
    cout << cars.top();
    return 0;
}
























