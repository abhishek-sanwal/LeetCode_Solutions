class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        rear = front = count = 0
        
        for rear in range(len(s)):
            
            if rear - front + 1 == 3:
                
                if s[rear]!= s[rear-1] and s[rear-1] != s[front] and s[rear]!=s[front]:
                    
                    count += 1
                
                front += 1
                
        
        return count

        
        