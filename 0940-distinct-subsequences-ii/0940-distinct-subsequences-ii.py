class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        dp = [0]*26
        for i in s:
            
            dp[ord(i)-ord('a')] = sum(dp) + 1
            
        return sum(dp) % (10**9+7)
        
        dp = [1]
        
        # 0(26)
        mapp = {
        }
         
        for i in range(len(s)):
            
            dp.append(2*dp[-1])
            if s[i] in mapp:
                
                dp[-1] -= dp[mapp[s[i]]]
                
            mapp[s[i]] = i
            
        return (dp[-1] - 1) % (10**9+7)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        dp = [1]
        mapp = {}
        for i in range(len(s)):
            
            dp.append(dp[-1]*2)
            
            if s[i] in mapp:
                
                dp[-1] -= dp[mapp[s[i]]]
                
            mapp[s[i]] = i
            
        return (dp[-1]-1)%(10**9+7)
        
        
#         "abc"
        
#         dp[0] = 2 = ["","a"]
#         dp[1] = 4 = ["","a","b","ab"]
#         dp[2] = 8 = ["","a","b","c","ab","bc","ca","abc"]
        
#         so dp[i] = 2*dp[i-1] if ith charcter is not repeated
        
#         "aba"
        
#         dp[0] = 2 = ["","a"]   mapp = {"a":0}
#         dp[1] = 4 = ["","a","b","ab"]  mapp = {"a":0,b:"1"}
        
#         dp[2] = 6 ["","a","b","ab","ba","aa","aba"]

#             "aaa"  mapp = {a:0}
#             dp[0] = 2
#             dp[1] = 2*dp[1

