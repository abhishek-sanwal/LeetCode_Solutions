class Solution {
public:
    bool judgeSquareSum(int c) {
        
        int num =c;
        
        long low = 0, high = sqrt(num);
        
        while(low <= high){
            
            if(low*low + high*high > num) high--;
                
            else if(low*low + high*high < num) low++;
                
            else return true;
            
        }
        
        return false;
        
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