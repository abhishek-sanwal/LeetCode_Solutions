class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        return len(s.strip().split()[-1])
        
        length = 0
        
        i = len(s)-1
        
        while i>-1 and s[i] == " ":
            
            i-=1
            
        curr = i
        
        while i>-1 and s[i] != " ":
            i-=1
            
        return curr-i
        