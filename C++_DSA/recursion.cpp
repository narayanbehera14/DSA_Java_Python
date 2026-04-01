// #include<iostream>
// using namespace std;

// int sum(int k){
//     if( k > 0){
//         return k + sum(k - 1);
//     }
//     else {
//         return 0;
//     }
// }
// int main(){
//     int result = sum(100);
//     cout << result;
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int sum(int k){
//     if( k > 0){
//         return k + sum(k-1);
//     }
//     else{
//         return 0;
//     }
// }
// int main(){
//     int result = sum(0);
//     cout << "sum fo number : " <<result;
//     return 0;
// }


#include <iostream>
using namespace std;

int sum(int l){
    if(l > 0){
        return l + sum ( l - 1);  
    }
    else{
        return 0;
    }
}
    int main(){
        int num = sum(4);
        cout << "new sum = " <<num;
        return 0;
    }

.