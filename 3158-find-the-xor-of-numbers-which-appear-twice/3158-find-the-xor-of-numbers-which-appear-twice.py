class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        
        
        return reduce(lambda x,y:x^y,chain(set(nums),nums))
