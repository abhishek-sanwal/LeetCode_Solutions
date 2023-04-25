
# Maximum prefix average of array

from math import ceil
class Solution:
    def minimizeArrayValue(self, arr: List[int]) -> int:
        
        def valid(arr,mid):
            
            if arr[0] > mid:
                
                return False
            
            sumi = 0
            
            for i in range(len(arr)):
                sumi += mid - arr[i]
                if sumi <0:
                        return False
                    
            return True
        
        prefix_sum = 0
        
        ans = 0
        
        for i in range(len(arr)):
            
            prefix_sum += arr[i]
            
            ans = max(ans,ceil(prefix_sum/(i+1)))
        
        return ans
    
        start = 0
        end = 10**9
        
        while start <= end:
            
            mid = start + (end-start)//2
            
            if valid(arr,mid):
                print(mid)
                end = mid  - 1
                
            else:
                
                start = mid + 1
        
        return start
            
            
            