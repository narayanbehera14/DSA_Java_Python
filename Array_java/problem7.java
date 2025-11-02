//Insert an element at the beginning

public class problem7 {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        int[] newArray = new int[arr.length+1];

        for (int i = 0; i < 1; i++){
            newArray[i] = arr[i];
        }
        newArray[0] = 10;

        for (int i = 1 ; i < arr.length; i++ ) {
            newArray[i+1]= arr[i];

        }
        for (int i = 0; i < newArray.length; i++) {
            System.out.println(newArray[i]);
          
            
        }

    }
    
}
