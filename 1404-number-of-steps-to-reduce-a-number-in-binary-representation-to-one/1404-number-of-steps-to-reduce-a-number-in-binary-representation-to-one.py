class Solution:
    def numSteps(self, s: str) -> int:
        
        num = 0
        for i in range(len(s)-1,-1,-1):
            
            if s[i] == "1":
                
                # left shift
                num += (1<< (len(s)-i-1))
            
        print(num)
        opr = 0
        while num != 1:
            
            if num&1:
                
                num += 1
                
            else:
                # right shift
                num >>= 1
            
            opr += 1
            
        return opr