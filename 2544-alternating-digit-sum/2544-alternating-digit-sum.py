class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        sumi = 0
        
        x = str(n)
        
        for i in range(len(x)):
                       
            if i%2:
                sumi -= int(x[i])
                       
            else:
                sumi += int(x[i])
        
        return sumi
            
        
        sumi = 0
        
        count = 0
        
        while n:
            
            if count %2==1:
                
                sumi -= n%10
                
            else:
                sumi += n%10
            
            n//=10
            count +=1
            print(sumi)
        return sumi
            