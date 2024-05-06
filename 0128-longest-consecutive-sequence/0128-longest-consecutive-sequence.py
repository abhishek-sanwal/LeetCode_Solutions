class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
                
        
        
        ans = 1
        
        for i in nums:
            
            curr = 1
            
            ele = i
            
            while ele-1 in check:
                
                ele-=1
                curr+=1
                
            ele = i
            while ele+1 in check:
                curr+=1
                ele+=1
            check.add(i)
            ans = max(ans,curr)
        
        return ans
                