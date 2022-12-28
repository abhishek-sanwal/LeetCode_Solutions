class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        def bs(prefix,query):
            
#             if query < prefix[0]:
                
#                 return 0
            
#             elif query > prefix[-1]:
                
#                 return len(prefix)
            
            low = 0
            
            high = len(prefix) - 1 
            
            while low < high:
                
                mid = (low + high)//2
                
                if prefix[mid] == query :
                            
                    return mid + 1
                
#                 elif prefix[mid-1] < query and prefix[mid] > query:

#                     return mid
                
                if prefix[mid] > query:
                    
                    high = mid - 1
                
                else:
                    low = mid + 1
                                            
            #print(low,query,prefix)                                            
            return low if prefix[low] > query else low + 1
            
        nums.sort()
        
        prefix = [nums[0]]
        
        for i in range(1,len(nums)):
            
            prefix.append(prefix[i-1] + nums[i])
            
        # prefix = [1,3,7,11]
        ret = [bs(prefix,query) for query in queries]
        
        return ret
            
        
        
        
        
        
        
        
        
        
        
        
        