class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        # The prime decompisition of c should not contain 
        # prime decomposition does not contain any p^k
        # where prime p = 3 mod 4 and k is odd
        
        n = c
        
        low = 0*0
        
        high = int(c**0.5)
        
        while low <= high:
            
            left = low**2
            right = high**2
            
            if left + right < n:
                
                low += 1
                
            elif left + right > n:
                
                high -= 1
                
            else:
                
                return True
            
        return False
        
        
        for i in range(2,int(n**0.5)+1):
            
            if n%i==0:
                p = i
                k = 0
                while not n%i:
                    k += 1
                    n //= i
                
                if k%2 and p%4==3:
                    
                    return False
        
        return n%4!=3
        
        