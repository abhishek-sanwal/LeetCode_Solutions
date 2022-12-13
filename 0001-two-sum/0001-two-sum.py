class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        
        for idx,ele in enumerate(nums):
            
            if target - ele in hashmap:
                
                return [hashmap[target-ele],idx]
            
            hashmap[ele] = idx
        