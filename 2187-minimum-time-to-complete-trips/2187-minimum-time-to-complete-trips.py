class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        mini,maxi = min(time),max(time)
        low = 0
        
        high = maxi*totalTrips
        
        def valid(mid):
            
            trips = 0
            
            return sum(mid//curr_time for curr_time in time) >= totalTrips
        
        while low <= high:
            
            mid = (low+high)//2
            
            if valid(mid):
                
                high = mid - 1
                
            else:
                
                low = mid + 1
                
        return low