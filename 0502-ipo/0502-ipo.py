class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        heap = []
        projects = sorted(zip(profits, capital), key=lambda l: l[1])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= w:
                heapq.heappush(heap, -projects[i][0])
                i += 1
            if heap: w -= heapq.heappop(heap)
        return w
        
        # Find low capital max profit projects
        
        arr = [[i,-j] for i,j in zip(capital,profits)]
        
        arr.sort()
        
        ans = 0
        
        curr_wealth = w
        
        vis = set()
        # Find most profitable project requiring capital less than curr_wealth      
        for i in range(k):
            
            # Find leftmost index having wealth less than or equal to curr_wealth
            x = bisect_left(arr,[curr_wealth,1])
            
            while arr[x][2] in x:
                x -= 1
            
            curr_wealth += arr[x][0]
            ans += arr[x][1]
            vis.add(x)
            
        return ans
    
        