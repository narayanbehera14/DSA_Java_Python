// #include<iostream>
// using namespace std;

// void myfunction(){

//     cout<<"I just got executed!"<<endl;

// }
// void my();

// void names(){
//     cout<<"my name is liju:" <<endl;
// }
// int main(){
//     myfunction();
//     names();
//     my();
//     return 0;
// }

// void my(){
//     cout<<"this is a function:";
// }

#include<iostream>
#include<string>
using namespace std;

void myfunction(string fname) {
    cout << fname <<"refsnes\n";
}

int main() {
    myfunction("liju");
    
    return 0;
}