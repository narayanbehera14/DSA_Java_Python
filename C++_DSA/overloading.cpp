// #include<iostream>
// using namespace std;

// int plusFuncInt(int x, int y) {
//     return x + y ;
// }

// double plusFuncDouble(double x , double y) {
//     return x + y;

// }

// int main() {
//     int mynum = plusFuncInt(8,5);
//     double mynum1 = plusFuncDouble(3.2,3.4);

//     cout << "int : " <<mynum <<endl;
//     cout << " double = " << mynum1 <<endl;
//     return 0 ;
// }

#include <iostream>
using namespace std;

int num2 (int a , int b){
    return a + b;
}

double num2(double v , double r){
    return v + r;
}

int num2(int a,int b, int c){
    return a+ b+c;
}

int main(){
    int sum = num2(2,3);
    double sum2 = num2(10.2,5.5);

    int sum3 = num2(2,4,5);

    cout<< " trid number of sum is = " << sum3 <<endl;
    cout << " first sum is = " << sum << endl;
    cout << " second sum is = " << sum2 <<endl;
    return 0;
}