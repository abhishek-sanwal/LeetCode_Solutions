class Solution:
    def scoreOfString(self, s: str) -> int:
        
        sumi = 0
        
        for i in range(len(s)-1):
            
            sumi += abs(ord(s[i])-ord(s[i+1]))
            
        return sumi