class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i ,j = 0 ,0
        
        lis = []
        
        while i< len(word1) or j < len(word2):
            
            if i < len(word1):
                
                lis.append(word1[i])
                i+=1
                
            if j < len(word2):
                lis.append(word2[j])
                j+=1
                
        return "".join(lis)