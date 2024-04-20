class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def solve(s,j,k):
            
            count = 0
            
            while j>-1 and k<len(s) and s[j] == s[k]:
                
                count += 1
                j -= 1
                k += 1
                
            return count
                    
        
        count = len(s)
        
        for i in range(len(s)):
            
            # Count odd length
            count += solve(s,i-1,i+1) 
            
            # Count even length
            count += solve(s,i-1,i)
        return count
        
        
        #0(N^3)
        count = 0
        
        for i in range(len(s)):
            
            for j in range(i+1,len(s)+1):
                #print(s[i:j])
                if s[i:j] == s[i:j][::-1]:
                    
                    count += 1
        return count