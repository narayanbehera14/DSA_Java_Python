// #include <iostream>
// #include <string>

// using namespace std;
// int main(){
//     string greeting = " Hello and welcome " ;
//     string name = "To amity ";
//     name[1] = 'O'; 
//     string fullname = greeting.append(name);

//     string num = "20";
//     string num2 = "50";

//     string txt = "nandsjdlfsjdfjds";

//     cout << "The length of the txt string is : " <<txt.length() << endl;
//     cout << name[4] << endl;
//     cout << fullname << endl ;
//     cout << num + num2<<endl;
//     cout << num[num.length() - 1] << endl;
//     cout << num + name << endl;
//     cout << name <<endl;

//     return 0;
// }

// #include <iostream>
// using namespace std;
// #include <string>

// int main() {
//     string mystring = "Hello";
//     cout << mystring << endl;
//     cout << mystring.at(0) << endl;
//     cout << mystring.at(1) << endl;
//     cout << mystring.at(mystring.length() - 1) <<endl;

//     mystring.at(0) = 'j';
//     cout << mystring << endl;
//     return 0;
// }

#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main(){
    string txt = " it\'s alright";
    cout << txt <<endl ;
    string tt = "The character \\ is called backslash.";
    cout << tt;

    string firstname;
    cout << "Type your first name = ";
    cin >> firstname;
    cout << "your name is : " << firstname << endl;
    cout << max(5,10)<<endl;
    cout <<sqrt (64)<<endl;
    cout << log(2)<<endl;
    return 0;
}