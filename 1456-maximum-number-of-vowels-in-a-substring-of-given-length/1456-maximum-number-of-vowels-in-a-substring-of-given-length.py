class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        front = curr = maxi = 0
        
        vowels = ["a","i","e","o","u"]
        
        for rear in range(len(s)):
            
            if s[rear] in vowels:

                curr += 1
                
            
            if (rear - front)+1 == k:

                maxi = max(maxi,curr)
                
                if s[front] in vowels:
                    
                    curr -= 1
                
                front += 1
            
        return maxi
            
            
            