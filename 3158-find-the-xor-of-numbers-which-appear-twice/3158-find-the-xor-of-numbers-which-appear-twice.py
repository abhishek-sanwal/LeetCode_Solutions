class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        
        
        return reduce(lambda x,y:x^y,nums) ^ reduce(lambda x,y:x^y,set(nums))
        