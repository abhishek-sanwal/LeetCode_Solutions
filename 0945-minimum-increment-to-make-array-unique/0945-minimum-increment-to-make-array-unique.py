class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # [3,2,1,2,1,7]
        # [1,1,2,2,3,7]
        # [1,2,3,4,5,7]
        nums.sort()
        count = 0
        for i in range(1,len(nums)):

            if nums[i] <= nums[i-1]:
                
                x = nums[i-1] - nums[i]

                nums[i] += x +1
                count += x +1
            #print(nums)
        return count