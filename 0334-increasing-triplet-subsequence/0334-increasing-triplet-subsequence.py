class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
        
        small = 10**18
        maxi = -small
        
        for i in nums:
            
            
            small = max(maxi,small)
            maxi = max(maxi,i)
        
            if small != maxi:
                
                return True
            
        return False