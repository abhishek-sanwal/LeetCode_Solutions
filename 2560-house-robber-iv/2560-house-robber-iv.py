class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        if k==0:
            
            return 0
        
        def valid(mid):
            
            arr = nums
            
            take = i = 0
            
            while i < len(nums):
                
                if nums[i] <= mid:
                    
                    take += 1
                    
                    i+=2
                else:
                    i+=1
                #print(i,k,mid)
            return take >= k
        
        low = min(nums)
        
        end = sum(nums)
        
        while low <= end:
            
            mid = (low + end)//2
            
            if valid(mid):
                #print(mid)
                end = mid - 1
                
            else:

                low = mid + 1
                
        return low
                
        
        