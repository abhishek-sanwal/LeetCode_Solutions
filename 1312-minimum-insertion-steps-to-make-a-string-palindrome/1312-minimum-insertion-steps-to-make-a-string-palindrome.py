class Solution:
    def minInsertions(self, s: str) -> int:
        
        def LongetCommonSubsequence(s1,s2):
            
            dp = [[0]*(len(s1)+1) for _ in range((len(s2)+1))]
            
            for i in range(len(s1)):
                
                for j in range(len(s2)):
                    
                    if s1[i] == s2[j]:
                        
                        dp[i+1][j+1] = dp[i][j] + 1
                        
                    else:
                        
                        dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
                        
            lcs = dp[-1][-1]
            #print(lcs,dp)    
            return lcs
        
        return len(s) - LongetCommonSubsequence(s,s[::-1])
    
    
            
            