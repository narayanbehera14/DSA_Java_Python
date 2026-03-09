// #include <iostream>
// #include <string>
// using namespace std;
// int main( ){

// string cars[4] = {"volvo","BMW","FORD","mAZDA"};
// // cars[0] = "Nano";
// // cout << cars[0];
// for ( int i = 0; i<5 ; i++){
//     cout << cars[i] <<endl;
// }
// return 0;
// }

// #include <iostream>
// #include <string>
// using namespace std;
// int main() {
// string cars[5] = {"Volvo", "BMW", "Ford", "Mazda", "Tesla"};

// for (int i = 0; i < 5; i++) {
//   cout << i<< " = "<<  cars[i] << endl;
// }
// return 0;
// }


// #include <iostream>
// #include <string>
// using namespace std;
// int main() {
//     int number[4] = {2,3,5,6};
//     number[1] = 10;

//     int mynumber[3] = {11,22,33};
//     string cars[2] = {" LAMBO","FERRARI"};

//     for (int i = 0; i<2; i++){
//         cout << "cars names = " << cars[i] << endl;
//     }

//     for ( int i = 0; i < 3 ; i++){
//         cout << "mynumber is = " << mynumber[i] << endl;
//     }

//     for (int i = 0 ; i <4; i++){
//         cout<< " number is = " << number[i] <<endl;
//     }
//     return 0;
// }

// #include <iostream>
// #include <string>
// #include <vector>

// using namespace std;

// int main(){
    // string myCars[5];
    // myCars[0] = "Maruti";
    // myCars[1] = "honda";
    // myCars[2] = "Hyndia";
    // myCars[3] = "audi";
    // myCars[4] = "Benz";
    // for(int i = 0 ; i < 5; i++){
    //     cout << myCars[i] << endl;
    // }
//     vector<string> cars = {"volvo","bmw","ford"};
//     cars.push_back("tesla");
//     return 0; 
// }

// #include <iostream>
// #include<string>
// using namespace std;
// int main(){
//     int number[5] = {10,20,30,40,50};
//     int getarraylength = sizeof(number) / sizeof(number[0]);
//     cout << getarraylength;
//     // cout << sizeof(number);
//     return 0;
// }

// #include<iostream>
// #include<string>
// using namespace std;
// int main(){
//     int mynumber[3] = {11,22,33};
//     // for (int i = 0; i < 3; i++){
//     for (int i = 0; i < sizeof(mynumber)/ sizeof(mynumber[0]);i++) {
//         cout << " number is = " << mynumber[i] <<endl;
//     }
//     return 0;
// }

// #include <iostream>
// #include <string>
// using namespace std;
// int main(){
//     int num[3] = {11,22,33};
//     for (int num : num){
//         cout << num << endl;
//     }
//     return 0;
// }

#include <iostream>
#include<string>
using namespace std;
int main() {
    int ages[8] = {20,30,40,60,50,11,050,55};
    float avg, sum = 0;
    int  i;

    int length = sizeof(ages)/sizeof(ages[0]);

    int lowestage = ages[0];
    for(int age : ages){
        if(lowestage < age){
            lowestage = age;  
        }
    }
    cout << "The lowest age is: "<< lowestage <<endl;

    // for(int age : ages){
    //     sum += age;

    // }
    // avg = sum / length;
    // cout << " the average age is : " << avg << "\n";
    return 0;
}