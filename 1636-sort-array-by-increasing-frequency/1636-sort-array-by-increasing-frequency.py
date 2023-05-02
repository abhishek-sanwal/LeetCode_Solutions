class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        x = Counter(nums)
        
        nums.sort(key=lambda z:(x[z],-z))
        
        return nums