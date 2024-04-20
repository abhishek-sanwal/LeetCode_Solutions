class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        
        def backTracking(curr_sum,idx,curr_list):
            
            if curr_sum > target or idx == len(candidates):
                
                return None
            #print(curr_sum,curr_list)
            if curr_sum == target:
                
                ans.append(curr_list[:])
            
            for j in range(idx,len(candidates)):
                
                curr_list.append(candidates[j])
                backTracking(curr_sum + candidates[j],j,curr_list)
                curr_list.pop()
                
            return None
        
        backTracking(0,0,[])
        
        return ans
                