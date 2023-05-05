class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        curr = maxx =1
        
        for i in range(1,len(s)):
            
            if ord(s[i]) -ord(s[i-1]) == 1:
                
                curr += 1
            else:
                curr = 1
                
            maxx = max(maxx,curr)
            
        return maxx
        
        