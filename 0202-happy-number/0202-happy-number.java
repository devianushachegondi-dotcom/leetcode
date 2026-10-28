class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> set=new HashSet<>();
      
        while(n!=1){
            if(set.contains(n)){
                return false;
            }
        
            set.add(n);
            int sum=0;
            int temp=n;
        while(temp>0){
            int dig=temp%10;
           
            sum=sum+dig*dig;
             temp=temp/10;
        }
        n=sum;
        }
        return true;
    }
}