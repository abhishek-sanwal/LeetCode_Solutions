class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
#         nums = [1,3,2,3,3], k = 2
        
#         [1] => 1 count =1
#         [1,3,2] => 3 count =6
#         [1,3,2,3] => [2,3] count = 8
#         [2,3,3] => [3]  count = 9
        
#         [1], [3],[2],[3],[3] done
#         [1,3],[3,2],[2,3] done
#         [1,3,2]  done
        
#         [1,3,2,3,3]
        
#         [1,3,2,3], [3,2,3,3] done
        
#         [3,2,3], [2,3,3] done
        
#         [3,3] done
        
        front = count = 0
        
        counter = Counter()
        
        maxi = max(nums)
        
        for rear in range(len(nums)):
            
            counter[nums[rear]] += 1
            
            while counter[maxi] >= k:
                
                counter[nums[front]] -= 1
                
                front += 1
                
            count += (rear-front+1)
            
        total_subarrays = ( len(nums) * (len(nums)+1)) // 2
        # print(total_subarrays)
        
        return total_subarrays - count
                
            
            
        
        
        
        
        
#         nums = [1,3,2,3,3], k = 2
        
#         [1,3,2,3] count = 1
#         [3,2,3] count = 2 skipped = 1
#         [3,2,3,3] count = 3
#         [2,3,3] count = 4 skipped = 2
#         [3,3] count = 5 skipped = 3
        
#         [1,3,2,3,3]
        
        
        