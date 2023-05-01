class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        m = max(nums)
        m-=1
        return ((m+k)*(m+k+1))//2 - (m*(m+1))//2