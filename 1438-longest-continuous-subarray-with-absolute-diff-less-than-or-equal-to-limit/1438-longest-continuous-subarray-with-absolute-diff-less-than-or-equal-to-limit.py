class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
#         [2,] min_deque ascending
#         [10] max_deque deseding
#         max_deque descending
#         min_deque asscending
        
#         [8,2,4,7]
        
#         sub   max  min
#         [8]   [8]  [8]
#         [8,2] [8,2] [2] 8-2 > 4 
#         [2]   [2]  [2]
#         [2,4] [4]   [2,4] 4-2 < 4 maxi = 2
#         [2,4,7] [7] [2,4,7] 7-2 > 5 maxi = 2
#         [4,7]  [7]  [4,7] 7-4 <4  maxi =2
        
        
#         [10,1,2,4,7,2]
        
#         sub max min
        
#         [10] [10] [10]
#         [10,1] [10,1] [1] 10-1 >5 
#         [1]  [1] [1]  maxi =1 
#         [1,2] [2] [1,2] 2-1 <5 maxi =2
#         [1,2,4] [4] [1,2,4] 4-1 <5 maxi =3
#         [1,2,4,7] [7] [1,2,4,7] 7-1 > 5
#         [2,4,7] [7] [2,4,7] 7-2<=5 maxi =4
        
#         [2,1]
        
        # should be ascending order
        min_deque = deque()
        
        # should be descending order
        max_deque = deque()
        
        front = maxi = 0
        
        for rear in range(len(nums)):
            
            while min_deque and nums[rear] < min_deque[-1]:
                min_deque.pop()
            
            min_deque.append(nums[rear])
            
            while max_deque and nums[rear] > max_deque[-1]:
                max_deque.pop()
                
            max_deque.append(nums[rear])
            # print(max_deque, min_deque)
            while max_deque and min_deque and max_deque[0] - min_deque[0] > limit:
                if nums[front] == max_deque[0]:
                    max_deque.popleft()
                    
                if nums[front] == min_deque[0]:
                    min_deque.popleft()
                    
                front += 1
            # print(max_deque, min_deque)
            maxi = max(maxi,rear-front+1)
            
        return maxi
            