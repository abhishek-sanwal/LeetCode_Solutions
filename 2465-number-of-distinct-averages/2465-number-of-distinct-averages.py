
from heapq import *
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
        nums.sort()
        
        i = 0
        
        j = len(nums)-1
        
        check = set()
        
        while i<j:
            
            x = nums[i]
            y = nums[j]
            i += 1
            j-=1
            check.add((x+y)/2)
        
        
        return len(check)
        
        