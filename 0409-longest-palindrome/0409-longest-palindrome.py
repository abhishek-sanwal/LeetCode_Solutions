class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        chars = [0]*52
        
        for i in s:
            
            # character is uppercase
            if ord(i) < ord('a'):
                
                chars[26 + (ord(i)-ord('A'))] += 1
                
            else:
                
                chars[ord(i)-ord('a')] += 1 
            
            
        odd = count = 0
        
        for i in range(52):
            
            count += chars[i]-1 if chars[i] & 1 else chars[i]
            
            if chars[i] & 1:
                
                odd = 1
        
        return count + odd
            