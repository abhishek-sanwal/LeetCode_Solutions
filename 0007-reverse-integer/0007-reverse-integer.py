class Solution:
    def reverse(self, x: int) -> int:
        
        sign = x>=0
        
        x = abs(x)
        
        reverse_num = 0
        
        limit = 1 << 31
        #print(limit)
        
        while x:
            
            digit = x % 10
            
            if reverse_num > limit//10 or reverse_num == limit//10 and digit>7:
                
                return 0
            
            reverse_num = (reverse_num * 10) + digit
            
            x //= 10
            
        return reverse_num if sign else reverse_num*-1
    
            
            
            