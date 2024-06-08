class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
#         nums = [23,2,4,6,7] k =6
#         nums = [5,2,4,0,1]
        
#         nums = [10,2,6,4,7] k =13
        
#         (0,i) => x
#         (0,j) => y
#         (i,j) => y-x
#         -------> prefix_sum = x
#         -------------------------->prefix_sum = y
#                  ------------------> prefix_sum=y
#                                     - prefix_sum = x
        
        
#         find a subarray sum divisible by k
        
#         3 loops bruteforce try out all subarrays
#         prefix sum 0(N) and then i,j =>0(N2)
        
#         [4,4,4,4,4] k = 5
#         vis = {4,8,12,16,18,20}
        prefix_sum = 0
        
        vis = set()
        
#         [23,2,6,4,7] = 6
#         [5,2,0,4,1]
        
#         mapp = {}
#         prefix_sum = 5 ,
#         mapp ={5}
#         prefix_sum = 1
#         mapp ={5,1}
#         prefix_sum = 5
        
        count_zeros = 0
        max_zeros = 0
        for i in range(len(nums)):
        
            # 1-length subarray is not allowed as a solution.
            if not nums[i]%k or not nums[i]:
                count_zeros += 1
                max_zeros = max(max_zeros,count_zeros)
                continue    
            else:
                count_zeros = 0
            
            prefix_sum += (nums[i] % k)
            
            prefix_sum %= k
            if prefix_sum in vis or not prefix_sum:
                
                return True
            
            vis.add(prefix_sum)
        max_zeros = max(max_zeros,count_zeros) 
        return max_zeros > 1
            
            
            
            
            
            

            