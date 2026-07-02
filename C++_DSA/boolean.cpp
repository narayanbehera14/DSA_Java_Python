#include <iostream>
using namespace std;
int main(){
    bool iscodingfun = true;
    bool isfishtasty = false;

    cout << iscodingfun <<endl;
    cout << isfishtasty<<endl;
    return 0;
}
 
#include<iostream>
using namespace std;
int main(){
    bool iscoding = false;
    bool isfish = true;

    cout << iscoding <<endl;
    cout << isfish <<endl;
    return 0;
}

#include <iostream>
using namespace std;

int main(){
    int x = 10;
    int y = 55;
    bool isgreater = x > y;
    cout << isgreater <<endl ;

    cout << (x < y )<<endl;
    cout << (x == y ) << endl;

    return 0;
}

#include<iostream>
using namespace std;
int main (){
    int a = 10;
    int n = 55;
    bool isbig = a > n;
    cout <<isbig <<endl;
    cout <<(n < a) <<endl;
    cout <<(n == a) <<endl;
    return 0;
}

// #include <iostream>
// using namespace std;

// int main(){

//         int myage = 25;
//         int voting = 18;

//         if(myage >= voting) {
//             cout << "old enough to vote!";

//         } else {
//             cout << "not old enough to vote,";

//         }

//         return 0;
//     }

#include<iostream>
using namespace std;
int main(){
    int myage = 25;
    int voting = 27;

    if(myage >= voting){
        cout << "old enough to vote!";
    }else{
        cout << "not old enough to vote";
    }
    return 0;
}

// #include <iostream>
// using namespace std;
// int main() {
//     int time = 20;
//     if (time > 10){
//         cout << "yes time is greater"<<endl;

//     } else {
//         cout << "no , time is not greater : "<<endl;
//     }
//     return 0;
// }
#include<iostream>
using namespace std;
int main(){
    int time = 20;
    if(time > 10){
        cout << "yes time is greater"<<endl;
    }else{
        cout << "no,time is not grater : "<<endl;
    }
    return 0;
}
// #include <iostream>
// using namespace std;
// int main(){
//     int time = 16;
//     if (time < 12){
//         cout << "Good day" <<endl;

//     } else if(time > 18){
//         cout<<"Good evening.";
//     }else{
//         cout<<"good afternoon";
//     }

//     return 0;
// }

#include <iostream>
using namespace std;

int main(){
    int time = 10;
    bool daytime = 12;
    bool nighttime = 9;

    if(daytime < time){
        cout << "good time for lunch";
    }else if(nighttime > time){
        cout <<"good time for dinner";
    }else{
        cout <<"good time for breakfeast";
    }
}














