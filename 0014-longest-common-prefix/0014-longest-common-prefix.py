class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp = []
        
        for i in range(len(strs[0])):
            
            char = strs[0][i]
            
            count = 1
            for j in range(1,len(strs)):
                
                if i<len(strs[j]) and strs[j][i] == char:
                    
                    count += 1
                    
                else:
                    
                    break
            
            if count == len(strs):
                lcp.append(char)
                
            else:
                break
        
        return "".join(lcp)
        