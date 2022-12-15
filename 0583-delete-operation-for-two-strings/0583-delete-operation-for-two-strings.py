class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        
        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        #print(dp)
        
        for i in range(1,len(text2)+1):
            
            char_text2 = text2[i-1]
            
            for j in range(1,len(text1)+1):
                
                char_text1 = text1[j-1]
                
                if char_text1 == char_text2:
                    
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else:
                    
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        #print(dp)
        x =dp[-1][-1]
        
        return len(text1) + len(text2) - 2*x
        