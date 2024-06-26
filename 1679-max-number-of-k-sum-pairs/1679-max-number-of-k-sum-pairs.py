class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
#         count = 0
        
#         mapp = Counter()
        
#         for i in nums:
            
#             if k-i in mapp:
                
#                 count += mapp[k-i]
#                 mapp[k-i] -= 1
                
#             mapp[i] += 1
                
#         [1,2,3,4]
#         return count
        
        
        
        
        
        
        
        
        count = 0
        # [1,3,3,3,4]
        low = 0
        high = len(nums)-1
#         [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
#         [1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5,5]
        
        nums.sort()
        while low < high:
            # print(nums[low],nums[high])
            if nums[low] + nums[high] == k:

                low += 1
                high -= 1
                count += 1
            
            elif nums[low] + nums[high] > k:

                high -= 1

            else:
                low += 1

        return count