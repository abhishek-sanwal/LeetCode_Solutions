class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        curr = 1
        ans =  0
        
        for i in range(1,len(prices)):
            
            if prices[i] == prices[i-1] -1:
                
                curr += 1
                
            else:
                #print(curr)
                ans += (curr * (curr+1))//2
                curr = 1
        
        return ans + (curr*(curr+1))//2
            
            