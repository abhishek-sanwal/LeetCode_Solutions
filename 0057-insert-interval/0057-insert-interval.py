class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        low = 0
        high = len(intervals) - 1
        
        while low <= high:
            
            mid = (low + high)//2 
            if intervals[mid][0] < newInterval[0]:
                low = mid + 1
                
            else:
                high = mid - 1
        ans = []
        
        intervals.insert(low,newInterval)
        
        for a,b in intervals:
            
            if ans and ans[-1][1] >= a:
                ans[-1][1] = max(ans[-1][1],b)
                
            else:
                ans.append([a,b])
                
        return ans
            
        
            