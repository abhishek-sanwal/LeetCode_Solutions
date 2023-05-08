class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        def valid(mid,nums):
            
            count = 0
            
            for i in nums:
                
                if i<=mid:
                    
                    count +=1
            
            return count>mid
        
        low = 1
        
        high = len(nums)
        
        while low <= high:
            
            mid = (low + (high-low)//2)
            
            if valid(mid,nums):
                
                high = mid - 1
                
            else:
                
                low = mid + 1
        
        return low
        
        fast = slow = nums[0]
        
        while True:
            
            fast = nums[nums[fast]]
            
            slow = nums[slow]
            
            if fast == slow:

                break
            
            print(fast,slow)
        
        slow = nums[0]
        
        while slow != fast:
            
            print(fast,slow)
            fast = nums[fast]
            
            slow = nums[slow]
        
        return fast