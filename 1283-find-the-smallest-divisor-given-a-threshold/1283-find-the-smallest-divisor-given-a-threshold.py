class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def valid(mid):
            
            return sum(ceil(num/mid) for num in nums) <= threshold

        low = 1

        high = sum(nums)

        while low <= high:

            mid = (low +(high-low)//2)

            if valid(mid):

                high = mid - 1

            else:
                low = mid + 1

        return low
        
        