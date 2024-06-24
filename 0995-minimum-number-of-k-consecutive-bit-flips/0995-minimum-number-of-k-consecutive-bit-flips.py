class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        que = deque()
        count = 0
        # [1,1,0] k =2
        # [0] []
        # [0,1,1] k =2
        # [1,0,1]
        # [1,1,0]         
        # [0] [0] count = 1
        # [1] []
        for i in range(len(nums)):
            
            while que and i-que[0] >= k:
                que.popleft()

            if len(que)%2:
                nums[i] ^= 1

            if nums[i] == 0:
                
                if i > len(nums)-k:
                    return  -1
                que.append(i)
                count += 1
        return count
            

       # I need to know that I have fliped the next
        # k elements 
        # nums = [0,0,0,1,0,1,1,0], k = 3
        # [0] [0,0,0,1,0,1,1,0]
        # [0] [0,0,0,1,0]


        # [0,1,0] sum=1
        # [1,0,1] sum=2

        # 0(N^2)
        # 0(1)
        # count = 0
        # for i in range(len(nums)-k+1):
        #     if nums[i] == 0:
        #         count += 1 
        #         for j in range(i,i+k):
        #             nums[j] ^= 1
        
        # return count if not nums.count(0) else -1