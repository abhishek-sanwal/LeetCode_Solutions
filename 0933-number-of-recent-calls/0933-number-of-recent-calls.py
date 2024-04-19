from bisect import bisect_left, bisect_right
class RecentCounter(object):

    def __init__(self):
        
        self.arr = deque()
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        
        self.arr.append(t)
        x = bisect_left(self.arr,t-3000)
        
        if x == len(self.arr):
            
            return 0
        ans = len(self.arr) - x
        idx = 0
        while idx < x:
            self.arr.popleft()
            idx += 1
    
        return ans
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)