function reverseNumber(n){
    let left = 0;
    let right = n.length - 1;
    
    while(left < right){
        let temp = n[left];
        n[left] = n[right];
        n[right] = temp

        left++;
        right--
    }
    console.log(n)
    
}


reverseNumber([1, 2, 3, 4, 5])