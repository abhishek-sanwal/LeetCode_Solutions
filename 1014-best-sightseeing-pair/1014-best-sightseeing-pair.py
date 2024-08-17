class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
#         nums[i] + nums[j] + i-j
#         nums[i] + i + nums[j] - j
            
        right = [0]*len(values)
        
        prev = maxi = values[-1] - (len(values)-1)
        
        for i in range(len(values)-2,-1,-1):
            
            maxi = max(maxi,values[i] + i + prev)
            
            prev = max(prev, values[i]-i)
            
        return maxi
        
        right[-1] = maxi = values[-1] - (len(values)-1)
        
        for i in range(len(values)-2,-1,-1):

            
            right[i] = max(right[i+1]-1, values[i])

        for i in range(len(values)-1):
            
            maxi = max(maxi, values[i] -1 + right[i+1])

        return maxi