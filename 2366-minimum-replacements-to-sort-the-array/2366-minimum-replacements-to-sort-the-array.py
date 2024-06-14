class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        
#                <-----
            
#         Non-decreasing from left to right
#         Non-increasing from right to left
    
        # 15 => 3, 12 => 3,3,9 => 3,3,3,6 => 3,3,3,3,3
        
        def count_operations(current, desired):
            
            oprs = ceil(current / desired)

#         # (k - 1) is the minimum number of times you'll have to split
#         ret += k - 1
#         # (num // k) is the maximal number you can create from splitting (k - 1) times
#         prev = num // k
            
#             oprs = ceil(current/desired) 
            
            return [ current//oprs ,oprs-1]
            
            
#         [12,9,7,6,17,19,21]
#         [12,9,3,4,6,17,19,21] opr = 1
#         [12,3,3,3,4,6,17,19,21] opr = 3 (+2)
#         [3,3,3,3,3,3,3,3,3,4,6,17,19,21] opr = 6 (+3)
            
        previous_element = nums[-1] 
        cost = 0
        for i in range(len(nums)-2,-1,-1):
            
            # Can not be increasing
            if nums[i] > previous_element:
                
                previous_element,oprs = count_operations(nums[i], previous_element)
                cost += oprs
            else:
                previous_element = nums[i]
        return cost
        
        
        
#         7 => 2 5(1) => 2,3,2 (2) =>[1,1,2,2] (3)
#         3 => 2,1 (1) => 1,1,1 (2)
#         [2,3,7,2]
#         [2,3,1,1,2,2,2]
#         [2,1,1,1,1,1,2,2,2]
#         []
        
        
        
#         [2,1,2,7,2]
#         [1,1,1,2,7,2]
#         [1,1,1,2,3,4,2]
#         [1,1,1,2,1,2,2,2,2]
#         [1,1,1,1,1,1,2,2,2,2]
        
#         [2,3,7,2]
        
#         [2,3,7,2]
        
#         [1,1,2,1,7,2]
#         [1,1,1,1,1,7,2]
#         [1,1,1,1,1,3,4,2]
#         [1,1,1,1,1,1,2,4,2]
#         [1,1,1,1,1,1,1,1,4,2]
#         [1,1,1,1,1,1,1,1,2,2,2]
        