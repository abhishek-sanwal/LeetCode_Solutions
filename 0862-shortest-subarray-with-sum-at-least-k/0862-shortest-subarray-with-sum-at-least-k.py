class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
#         prefix[j] -prefix[i] >= k and j-i is minimized.
        
#         prefix[j] >= prefix[i]
#         prefix[j] - k >= prefix[i]
#         pass
    
#         x1 < x2 and p[x2] <= p[x1]

        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n): 
            prefix[i + 1] = prefix[i] + nums[i]
            
        d = collections.deque()
        res = n + 1
        for j in range(n + 1):
            # prefix[d[0]] contains i so prefix[j]-prefix[i] >= k
            while d and prefix[j] <= prefix[d[-1]]: 
                d.pop()
            while d and prefix[j] - prefix[d[0]] >= k: # d contains i's
                res = min(res, j - d.popleft())
            # print(d,"before")
            d.append(j)
            # print(d,"after")
        return -1 if res==n+1  else res