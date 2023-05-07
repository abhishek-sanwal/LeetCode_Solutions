class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        pow = 10**k
        n =  num
        count =  0
        
        while n:
            
            d = n%pow
            print(d,n,pow)
            if d and num%d==0:
                
                count += 1
            
            if n//pow==0:
                break
            
            n //= 10
            
        
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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