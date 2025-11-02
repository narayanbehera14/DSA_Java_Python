// Insert an element at a specific index

public class problem6 {
    public static void main(String[] args) {
        
        int[] arr = {1,2,3,4,5};
        int[] newArray = new int[arr.length + 1];
        // insert element 44 at index 3

        

        for (int i = 0; i < 3; i++){
            newArray[i] = arr[i];
        }

        newArray[3] = 44;

        for(int i = 3; i < arr.length; i++){
            newArray[i + 1] = arr[i];
        }

        for (int i = 0; i < newArray.length; i++){
            System.out.println(newArray[i]);
        }
    }

}