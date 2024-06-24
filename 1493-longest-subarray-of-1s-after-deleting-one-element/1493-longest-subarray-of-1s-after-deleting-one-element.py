class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # Window can have atmost one zero element
        
        maxi = front = count = 0
        
        for rear in range(len(nums)):

            if nums[rear] == 0:
                
                count += 1

            # Invalid window
            if count > 1: 
                count -= 1
                while nums[front] != 0:
                    front += 1

                front += 1
            # print(rear,front)
            maxi = max(maxi,rear-front)

        return maxi

