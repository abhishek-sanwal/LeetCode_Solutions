class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x:x[1])
        
        last = -math.inf
        
        count = 0
        
        for i in intervals:
            
            if i[0] >= last:
                
                last = i[1]
                count += 1
                
        return len(intervals)  -count
        
        
        