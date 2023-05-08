class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
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