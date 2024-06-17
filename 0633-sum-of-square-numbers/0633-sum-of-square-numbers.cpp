class Solution {
public:
    bool judgeSquareSum(int c) {
        
        int num =c;
        
        for(int i=2;i<sqrt(num);++i){
            
            if(!(num%i)){
                
                int p=i,k=0;
                
                while(!(num%i)){
                    
                    num /= i;
                    k++;
                }
                
                if(k%2 and p%4==3)  return false;
                
            }
            
        }
        
        return num %4 != 3;
    }
};