class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        #print(sum(int(i) for i in nums))
        
        digit_sum = 0
        
        for i in nums:

            while i:
                
                digit_sum += i%10
                i//=10
        
        return abs(sum(nums)-digit_sum)