class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        def is_similar_strings(s1,s2):
            
            count = 0
            for i in range(len(s1)):
                
                if s1[i] != s2[i]:
                    
                    count += 1
                    
            return count in [0,2]
        
    
        def dfs(i):
            
            vis[i] = True
            
            for j in range(len(strs)):
                
                if not vis[j] and is_similar_strings(strs[i],strs[j]):
                    
                    dfs(j)
    
            return None
        
        components = 0
        
        vis = [0]*len(strs)
        
        for i in range(len(strs)):
            
            if vis[i]:
                continue
            
            #print(i)
            components += 1
            dfs(i)
            
        return components
        
        
            