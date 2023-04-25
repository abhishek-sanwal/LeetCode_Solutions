from collections import *
class Solution:
    def partitionString(self, s: str) -> int:
        
        #return max(Counter(s).values())
        
        check = set()
        
        c = 1
        
        i = 0
        
        while i < len(s):
            
            if s[i] in check:
                
                check = set()
                check.add(s[i])
                c += 1
                
            else:
                
                check.add(s[i])
            
            i += 1
            
        return c
        