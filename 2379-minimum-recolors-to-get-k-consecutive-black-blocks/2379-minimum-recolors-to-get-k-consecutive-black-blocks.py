
# Sliding Window Solution to get minimum.
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        front = curr = maxi = 0
        s = blocks
        for rear in range(len(s)):
            
            if s[rear] =="B":

                curr += 1
                
            if (rear - front)+1 == k:

                maxi = max(maxi,curr)
                
                if s[front] =="B":
                    
                    curr -= 1
                
                front += 1
            
        return k-maxi
                    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        