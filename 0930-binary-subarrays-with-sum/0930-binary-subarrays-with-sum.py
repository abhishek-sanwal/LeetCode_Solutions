class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        prefix_sum = 0
        
        mapp = defaultdict(int)
        
        count = 0
        
        for element in nums:
            
            prefix_sum += element
            
            if prefix_sum == goal:
                count += 1
                
            if prefix_sum - goal in mapp:
                
                count += mapp[prefix_sum -goal]
                
            mapp[prefix_sum] += 1
            
        return count