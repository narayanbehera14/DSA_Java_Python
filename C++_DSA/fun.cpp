// // #include<iostream>
// // using namespace std;

// // void myfunction(){

// //     cout<<"I just got executed!"<<endl;

// // }
// // void my();

// // void names(){
// //     cout<<"my name is liju:" <<endl;
// // }
// // int main(){
// //     myfunction();
// //     names();
// //     my();
// //     return 0;
// // }

// // void my(){
// //     cout<<"this is a function:";
// // }

// #include<iostream>
// #include<string>
// using namespace std;

// void myfunction(string fname) {
//     cout << fname <<"refsnes\n";
// }

// int main() {
//     myfunction("liju");
//     myfunction("jenny");
//     myfunction("anja");    
//     return 0;
// }

// #include<iostream>
// using namespace std;

// void myfunction(string country = "norway") {
//     cout << "country name = " << country <<endl;

// }

// int main() {
//     myfunction("sweden");
//     myfunction("india");
//     myfunction();
//     myfunction("USA");
//     return 0;
// }


// #include<iostream>
// using namespace std;

// void myfunction(string fname, int age) {
//     cout << fname << "fname" <<age << "year old "<<endl;
// }

// int main() {
//     myfunction("liju",5);
//     myfunction("amar" , 22);
//     myfunction("behera",41);
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int myfunction(int x) {
//     return 5 + x ;

// }

// int main() {
//     cout << " value after adding = " << myfunction(22);
//     return 0;
// }

// #include <iostream>
// using namespace std;

// void myfunction(int x){
//     cout << 5 + x ;

// }
// int main() {
//     myfunction(21);
//     return 0 ;
// }

// #include<iostream>
// using namespace std;

// void myfunction(int x , int y) {
//     cout << x + y ;
// }

// int main() {
//     myfunction(3 , 5);
//     return 0;
// }

// #include<iostream>
// using namespace std;

// void myfunction(int x , int y){
//     cout << x + y ;
// }

// int main() {
//     myfunction(3,4);
//     return 0;
// }

// #include<iostream>
// using namespace std;

// int myfunction(int x , int y) {
//     return x + y ;

// }

// int main() {
//     int z = myfunction(5,6);
//     cout << z <<" is addition number  ";
//     return 0;
// }

// #include <iostream>
// using namespace std;

// int doublegame(int x) {
//     return x * 2;

// }
// int main(){
//     for (int i = 1 ; i <= 5 ; i++){
//         cout << "double off "<< i << " is = " <<doublegame(i) <<endl;
//     }
//     return 0 ;
// }

// #include<iostream>
// using namespace std;

// void changevalue(int & num) {
//     num = 50;
// }
// int main() {
//     int value = 10;
//     changevalue(value);
//     cout <<value;
//     return 0 ;
// }


// #include<iostream>
// using namespace std;

// void swapNums(int &x , int &y){
//     int z = x;
//     x = y;
//     y = z;
// }

// int main() {
//     int firstNum = 10;
//     int secondNum = 0;

//     cout << " before swap: " <<"\n";
//     cout << firstNum << secondNum << "\n";

//     swapNums(firstNum,secondNum);

//     cout <<"after swap:" <<"\n";
//     cout << firstNum << secondNum<<"\n";

//     return 0 ;
// }

// #include<iostream>
// using namespace std;

// void myfun(int myfun[5]){
//     for (int i = 0; i < 5;i++){
//         cout << myfun[i] << endl;
//     }
// }


// #include<iostream>
// using namespace std;
// struct Car {
//     string brand;
//     int year;
// };

// void myfun(Car c ){
//     cout << " brand : " << c.brand  << " year : "<<c.year<<endl;
// }

// int main(){
//     Car mycar = {"toyota",2000};
//     myfun(mycar);
//     return 0;
// }


#include<iostream>
using namespace std;

float tocelsius(
    float fahrenheit ) {
        return (5.0 / 9.0 ) * (fahrenheit - 32.0);

    }

    int main() {
        float f_value = 98.8;
        float result = tocelsius(f_value);

        cout << "Fahrenheit : " << f_value << " \n";
        cout << "convert fahrenheit to celsius : " << result<<"\n";
        return 0 ;
    }
