class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        front = maxi = zeros = 0
            
        for rear in range(len(nums)):
            
            zeros += nums[rear] == 0
            while zeros > k:
                zeros -= nums[front] == 0
                front += 1

            maxi = max(maxi,rear-front+1)

        return maxi
    