from math import floor,ceil
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        x= [i for i in nums if i%6==0]
        
        if not x:
            return 0
        
        return floor(sum(x)/len(x))