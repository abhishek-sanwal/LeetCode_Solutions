class Solution:
    def maxValue(self, n: str, x: int) -> str:
        
        x = str(x)
        
        if n[0]!="-":
            
            for i in range(len(n)):
                
                if x>n[i]:
                    
                    return n[:i] + x + n[i:]
                
            return n + x
        
        else:
            for i in range(1,len(n)):
                
                if x<n[i]:
                    
                    return n[:i] + x + n[i:]
            
            return n + x