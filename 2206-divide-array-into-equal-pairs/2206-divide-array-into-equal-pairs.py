class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        x = Counter(nums)
        
        for i in x:
            
            if x[i]%2==1:
                
                return False
        return True

                