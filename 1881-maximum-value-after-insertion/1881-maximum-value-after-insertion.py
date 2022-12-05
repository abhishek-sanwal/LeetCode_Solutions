class Solution:
    def maxValue(self, n: str, x: int) -> str:
        
        start = 0 if n[0] != "-" else 1
        
        x = str(x)
        
        for i in range(start,len(n)):
            
            if not start and x > n[i]:
                
                return n[:i] + x + n[i:]
            
            elif start and n[i] > x:
                
                return n[:i] + x + n[i:]
            
        return n + x
                