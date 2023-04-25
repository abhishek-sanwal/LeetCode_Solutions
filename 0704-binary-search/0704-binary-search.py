class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        
        end = len(nums)-1
        
        while start <= end:
            
            mid = start + (end - start)//2
            
            if nums[mid] == target:
                
                return mid
            
            if nums[mid] > target:
                
                end = mid - 1
                
            else:
                start = mid + 1
        
        return -1
    
        if nums[0] == target:
            
            return 0
        
        # Put this if array is finit since while loop will give error
        if target < nums[0] or target > nums[-1]:
            
            return -1
        
        start = 0
        end = 1
        
        while target > nums[end]:
            
            temp = end + 1
            end = end+ (end - start+1)*2
            start = temp
        
        while start <= end:
            
            mid = start + (end-start)//2
            
            if nums[mid] == target:
                
                return mid
            
            if nums[mid] > target:
                
                end = mid -1
                
            else:

                start = mid + 1
            
        return -1
                
                

            
        