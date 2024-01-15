class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        maxi = ""
        s = num
        for i in range(len(num)-2):
            
            if s[i] == s[i+1] and s[i] == s[i+2]:
                
                maxi = max(maxi,s[i])
                
        return maxi*3
        
        