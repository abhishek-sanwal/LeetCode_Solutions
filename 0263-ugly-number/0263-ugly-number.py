class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n<=0:
            return False
        
        if n in {1,2,3,5}:
            
            return True
        
        for div in {2,3,5}:
            
            if n%div==0:
                
                while n%div==0:
                    n//=div
                    
        return n==1
            
        