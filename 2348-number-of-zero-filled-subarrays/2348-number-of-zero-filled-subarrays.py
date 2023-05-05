class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        ans = 0
        s = nums
        i = 0
        
        while i < len(s):
            
            if s[i] == 0:

                count = 0
                
                while i<len(s) and s[i]==0:
                    
                    count+=1
                    
                    i+=1
                #print(count,ans)
                ans += (count * (count+1))//2
            i+=1
        return ans