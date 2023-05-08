class Solution:
    def solve(self,intervals):
        
        intervals.sort()
        
        ret = []
        
        a,b = intervals[0][0] , intervals[0][1]
        
        for i in range(1,len(intervals)):
            
            if intervals[i][0] <= b:
                
                b = max(b,intervals[i][1])
                
            else:
                
                ret.append([a,b])
                a,b = intervals[i][0],intervals[i][1]
        
        ret.append([a,b])
        return ret
                
            
        
        return ret
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.solve(intervals)