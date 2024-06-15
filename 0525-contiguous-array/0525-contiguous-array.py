class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        
#         0,0,0,1,1,1 => sum of subarray should be lengeht of subarray divided by 2
        
        
#         pref[r] - pref[l-1] = (r-l)//2
        
#         2*pref[r] -r = 2*pref[l-1] * l
        
        
#         count indices where difference between indices is double of difference between elements
        
#     [0,1,0] 
#     at index 0 we are having odd zeros and even ones
#     at index 1 we are having even zeros and even ones
#     at index 2 we are having odd zeros and even ones
#     2-0

        count = max_length = 0
        
        mapp = {
            0:-1
        }
        
        for i in range(len(nums)):
            
            count += nums[i] if nums[i] ==1 else -1
            
            if count in mapp:
                
                
                max_length = max(max_length,i-
                                 mapp[count])
            else:
                                 
                mapp[count] = i
            
        return max_length
            
        