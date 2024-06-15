class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        def count_subarrays_with_max_atmost_x(x):
        
            front = count = 0

            for rear in range(len(nums)):

                if nums[rear] > x:

                    front = rear + 1
                    continue

                count += rear - front +1
            # print(count)
            return count
         
        return count_subarrays_with_max_atmost_x(right) - count_subarrays_with_max_atmost_x(left-1)
       