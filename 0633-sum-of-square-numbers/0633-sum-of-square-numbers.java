class Solution {
    public boolean judgeSquareSum(int c) {
        
        int num =c;
        
        for(int i=2;i<=(int)Math.sqrt(num)+1;++i){
            
            if(num%i==0){
                
                int p = i,k=0;
                while(num%i == 0){
                    
                    num /=i;
                    k++;
                    
                }
                if(k%2==1 && p%4==3)   return false;
                
            }
            
        }
        return num%4 != 3;
        
    }
}