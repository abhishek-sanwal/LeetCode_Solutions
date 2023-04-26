class Solution:
    def countEven(self, num: int) -> int:
        
        sumi = 0
        n =num
        while num:
            
            sumi += num%10
            
            num //=10
            
        return n//2 if sumi%2==0 else (n-1)//2