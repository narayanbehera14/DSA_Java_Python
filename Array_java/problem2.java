package DSA_JAVA_PYTHON ;

//Find the maximum and minimum element in an array

public class problem2 {
    public static void main(String[] args) {
        int [] arr = {1,2,5,6,8,10};
        int maximumelement = arr[0];
        int minimumelement = arr[0];

        for (int idx = 0; idx < arr.length; idx++) {
            if (maximumelement < arr[idx]) {
                maximumelement = arr[idx];
            }
            if ( minimumelement> arr[idx]){
                minimumelement = arr[idx];
            }
          
            
        }
         System.out.println("maximum element is :"  + maximumelement);
        System.out.println("minimum element is:"+ minimumelement);
    }
    
}
