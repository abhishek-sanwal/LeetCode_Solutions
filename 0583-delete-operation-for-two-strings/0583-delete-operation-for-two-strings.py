class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def lcs(text1,text2):
        
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
            
            return dp[-1][-1]
        
        
        return len(word1) + len(word2) - 2*lcs(word1,word2)
        