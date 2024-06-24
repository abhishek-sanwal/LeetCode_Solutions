class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
#         nums = [1,3,-1,-3,5,3,6,7] k=3
        
        
#         [1,3,-1] [3,-1]
        
#         [3,-1,-3] [3,-1,-3]
        
#         [-1,-3,5] [5]
        
#         [-3,5,3] [5,3]
        
#         [5,3,6] [6]
        
#         [3,6,7] [7]
        
        front = 0
        
        ans = list()
        
        que = deque()
        
        for rear in range(len(nums)):

            while que and que[-1] < nums[rear]:
                
                que.pop()
                
            que.append(nums[rear])
            
            while rear-front+1 > k:
                
                if que and que[0] == nums[front]:
                    
                    que.popleft()
                
                front += 1
            
            if rear-front+1 == k:
                
                ans.append(que[0])
                
        return ans
            