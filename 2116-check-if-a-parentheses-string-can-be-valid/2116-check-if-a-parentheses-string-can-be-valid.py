class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        s = [i for i in s]
        
        for i in range(len(locked)):
            
            if locked[i] == "0":
                
                s[i] = "*"
                
        print(s)
        
        open_count = close_count = 0
        
        high = len(s) - 1
        
        for low in range(len(s)):
            
            if s[low] in ["(","*"]:
                
                open_count += 1
                
            # Means we have matched this
            else:
                open_count -= 1
                
            if open_count < 0:
                return False
            
                
        for i in range(len(s)-1,-1,-1):
            
            if s[i] in [")","*"]:
                
                close_count += 1
                
            else:
                close_count -= 1
            
            if close_count < 0:
                return False
            
        return open_count %2 ==0 and close_count%2==0