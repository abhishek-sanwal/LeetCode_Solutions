class Solution:
    def numSteps(self, s: str) -> int:
        
        
        # 1101
        
#         if last bit is 1 add 2 to operations 
        
#         1+1 = 10 we will add 1 to that acc to operation
#         and remove last bit
        
#         1 + 1 = 1 2 operation + one bit
        
        
        carry = operations = 0
        
        for i in range(len(s)-1,0,-1):
            
            if int(s[i]) + carry == 1:
                
                operations += 1
                
                carry = 1
            
            operations += 1
            
        return operations + carry
                
            
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        num = 0
        # 0(N)
        for i in range(len(s)-1,-1,-1):
            
            if s[i] == "1":
                
                # left shift
                num += (1<< (len(s)-i-1))
            
        # 0(Log num)
        opr = 0
        while num != 1:
            
            if num&1:
                
                num += 1
                
            else:
                # right shift
                num >>= 1
            
            opr += 1
            
        return opr