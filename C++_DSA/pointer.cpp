// #include<iostream>
// using namespace std;
// int main() {
//     string food = "pizza";
//     string* ptr = &food;

//     cout << food <<endl;
//     cout << &food;
//     cout << *ptr <<endl;
//     *ptr = " narayan";
//     cout <<food<<endl;
//     return 0;
// }

// #include <iostream>
// using namespace std;

// int main() {
//     int mylist;
//     float myFloat;
//     double myDouble;
//     char myChar;

//     cout <<sizeof(myChar) <<endl;
//     cout <<sizeof(mylist) <<endl;
//     cout <<sizeof(myChar) <<endl;
//     cout << sizeof(myDouble) <<endl;
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int main() {
//     int* ptr = new int;
//     *ptr = 35;
//     delete ptr;
//     cout << *ptr;
//     return 0;
// }

#include<iostream>
#include<string>
using namespace std;

int main(){
    int numguest;
    cout << "enter guest no: "<<endl ;
    cin >> numguest;

    if(numguest <= 0 ){
        cout << "Number of guest must be at least 1.\n";
        return 0;
    }

    string* guests = new string[numguest];

    cin.ignore();

    for(int i = 0; i < numguest; i++){
        cout << "Enter name for guest " << (i+1) << ": ";
        getline(cin ,guests[i]);
    }

    cout << "\nGuest checked in:\n";
    for(int i = 0 ; i < numguest; i++){
        cout << guests[i] << "\n";
    }

    delete[] guests;
    return 0;
}