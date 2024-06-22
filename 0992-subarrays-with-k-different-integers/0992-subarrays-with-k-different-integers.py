class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def count_atmost_x(x):
            
            front = subarrays = 0
            
            count = Counter()
            
            for rear in range(len(nums)):
                
                count[nums[rear]] += 1
                
                while len(count) > x:
                    
                    count[nums[front]] -= 1 
                    if not count[nums[front]]:
                        del count[nums[front]]
                    
                    front += 1
                    
                subarrays += rear-front + 1
                # print(rear,subarrays,front)
            return subarrays
        
        return count_atmost_x(k) - count_atmost_x(k-1)
        
#         nums = [1,2,1,3,4], k = 3
        
#         [1,2,1,2,3] k =2
        
#         [1]
#         [1,2]
#         [2]
#         [1,2,1]
#         [2,1]
#         [1]
#         [1,2]
#         [1,2,1,2]
#         [2,1,2]
#         [2,3]
#         [2][3]
        
#         [2] 
       
        
        