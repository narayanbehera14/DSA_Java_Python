// #include <iostream>
// using namespace std;
// int main(){
//     int i = 0;
//     while (i < 5)
//     {cout << i << "\n";
//         i++;
//         /* code */
//     }
    
// }

// #include <iostream>
// using namespace std;
// int main(){
//     int countdown = 5;
//     while (countdown >= 0 ){
//         cout << countdown <<"\n";
//         countdown --  ;
//     }
//     {
//         cout << "happy new year!!" ;
//         /* code */
//     }
    
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int main(){
//     int number;
//     do{
//         cout << "type your number :";
//         cin >> number;
//     } while (number > 0);
    
//     return 0;

// }

// #include <iostream>
// using namespace std;
// int main(){
//     int i = 0 ;
//     while (i <= 10)
//     {cout << i << endl;
//         i += 2 ;
//         /* code */
//     }
    
//     return 0;
// }


#include <iostream>
using namespace std;

int main(){
    int dice = 1 ;
    while (dice <= 6){
        if (dice < 6)
        { cout << "no yatzy\n";
            /* code */
        } else {
            cout<< "yatxy\n";
        }
        dice = dice + 1 ;
        
    }
    return 0;
}