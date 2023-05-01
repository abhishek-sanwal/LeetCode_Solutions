class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        num = n
        sumi,prod = 0,1
        while num:
            
            sumi += num%10
            prod *= num%10
            num //= 10
            
        return prod - sumi