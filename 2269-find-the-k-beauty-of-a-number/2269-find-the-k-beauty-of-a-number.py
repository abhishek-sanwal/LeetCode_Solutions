class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        s = str(num)
        
        front = 0
        
        curr = 0
        
        count = 0
        
        for rear in range(len(s)):
            
            curr = curr*10 + (ord(s[rear])-48)
            
            if rear - front + 1 == k:
                
                if curr and num % curr == 0:
                    
                    count +=1
                    
                curr = curr - (ord(s[front])-48) * 10**(k-1)
                front +=1
            
        return count