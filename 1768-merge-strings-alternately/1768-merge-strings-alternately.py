class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i ,j = 0 ,0
        
        lis = []
        count = 1
        while i< len(word1) and j < len(word2):
            
            if count%2:
                
                lis.append(word1[i])
                i+=1
                
            else:
                lis.append(word2[j])
                j+=1
            count+=1
        
        
        while i<len(word1):
            
            lis.append(word1[i])
            
            i+=1
            
        while j<len(word2):
            
            lis.append(word2[j])
            
            j+=1
            
        return "".join(lis)