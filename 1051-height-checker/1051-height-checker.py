class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        return len([i  for i,j in zip(heights,sorted(heights)) if i != j])
        
        def counting_sort(heights):
            
            bucket = [0]*(101)
            
            for ele in heights:
                
                bucket[ele] += 1
                
            return bucket
        
        count = 0
        
        # arr = sorted(heights)
        
#         for i,j in zip(arr,heights):
            
#             if i != j:
                
#                 count += 1
                
#         return count

        bucket = counting_sort(heights)
        i = 1
        
        for element in heights:
            
            while bucket[i] == 0:
                
                i += 1
                
            if i != element:
                count += 1
            bucket[i] -= 1
                
        return count
            