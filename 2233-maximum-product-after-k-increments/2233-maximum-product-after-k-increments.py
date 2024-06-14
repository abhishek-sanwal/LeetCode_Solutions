class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        
        heapify(nums)
        
        for i in range(k):
            
            heappush(nums, heappop(nums) + 1)
        
        sol = 1
        mod = 10**9 + 7
            
        for i in nums:
            
            sol = (sol * i) % mod
            
        return sol
    
    