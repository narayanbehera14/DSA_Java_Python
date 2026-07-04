#include <iostream>
using namespace std;

int main(){
    // int sum = 0;
    // for (int i = 0 ; i <= 5; i++) {
    //     sum = sum + i; 

    // }
    // cout << "sum is = " <<sum;
    // for (int i = 0; i < 5; i++){
    //     cout<<i<<"\n";
    // }

//     for (int i = 10 ; i > 0 ; i--){
//         cout<<i <<"\n";
//     }

//     return 0;
// }

// #include<iostream>
// using namspace std;
// int main(){
//     int n = -45;
//     if(n >= 0) {
//         cout << "n is positive\n";
//     }else{
//         cout <<"n is negative\n";
//     }
//     return 0;

// }

#include<iostream>
using namspace std;
int main(){
    int age;
    cout <<" enter your age :"<<endl;
    cin >> age;
    if (age >= 18){
        cout<<"can vote\n";
    }else{
        cout<< "u cant vote\n";
    }
    return 0;
}

#include <iostream>
using namespace std;

    // int mynumber[5] = {10,20,30,04,50};
    // for (int num: mynumber){
    //     cout << num << "\n";
    // string word = "Hello";
    // for (char c : word) {
    //     cout << c << "\n";

    // }

    // for (int i = 0; i < 100; i++) {
    //     cout << i << "\n";
    // }

    // for ( int i = 0; i <= 10; i = i + 2){
    //     cout << i << endl;
    // }

    // for (int i = 2; i <=512 ; i *= 2){
    //     cout << i << "\n";
    // }

    int number = 2 ;
    int i;
    for (i = 1; i <= 10; i++) {
        cout << number << "x" << i << " = " << number * i << "\n";
        
    }
    return 0;
}

int n ;
cout <<"enter a number";
cin >> number;
if(n%2==0){
    cout <<"even number";
}else{
    cout <<"odd number";
}
return 0;
}

#include<iostream>
using namespace std;
int main(){
    int marks;
    cout<<" enter your marks:\n";
    cin>> marks;
    if(marks >= 90){
        cout <<"Grafe is A\n";
    }else if(marks >= 80 && marks <= 70){
        cout<< "Grade is B\n";
    }else if(marks >=60 && marks <= 50){
        cout <<"Grade is C";
    }else {
        cout <<"grade is C"
    } 
    return 0;
}