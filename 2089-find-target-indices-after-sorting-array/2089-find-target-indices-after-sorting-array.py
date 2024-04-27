class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        ele_count = great_count = 0
        
        for ele in nums:
            
            if ele == target:
                
                ele_count += 1
                
            elif ele > target:
                
                great_count += 1
                
        return [i for i in range(len(nums)-great_count-ele_count,len(nums)-great_count)]