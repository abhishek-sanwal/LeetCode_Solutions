class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def fun(x):
            
            if not x:

                return mapping[x]

            number = power = 0
            
            while x:
                
                number += (10**power) * mapping[x%10]
                power += 1
                x //= 10
            
            return number
        
        nums.sort(key=lambda x:fun(x))
        
        return nums