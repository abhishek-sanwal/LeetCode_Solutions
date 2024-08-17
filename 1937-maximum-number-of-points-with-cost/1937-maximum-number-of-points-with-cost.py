class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        row = len(points)
        col = len(points[0])

        dp = list()
        previous_dp = points[0]
        
        if row == 1:
            return max(points[0])
        # right i<j nums[i] + nums[j] - (j-i) = -j+i => nums[i] + i +  nums[j] - j
        # left i>j nums[i] + nums[j] - (i-j) = nums[i] - i + nums[j] + j
        # nums[i] + nums[j] - abs(i-j)
        # nums[i] + nums[j] - i -j (i>j)
        # nums[i] + nums[j] - j-i (j>i)
        # [1,5]
        # [1,6]  [4,5]
        for i in range(1,row):
            
            left = [previous_dp[0]]

            for j in range(1, col):

                left.append(max(left[-1], previous_dp[j] + j )) # i>j

            right = [0]*col
            right[-1] = previous_dp[-1] - (col-1)
        
            for j in range(col-2,-1,-1):

                right[j] = max(right[j+1], previous_dp[j] -j) # i<j
            # print(left, right)
            dp = []
            for j in range(col):
                maxi = -10**18
                                  
                maxi = max(maxi, points[i][j] + right[j] + j, points[i][j] + left[j]-j)
                
                dp.append(maxi)
            # print(dp)
            previous_dp = dp
            dp = list()
        
        return max(previous_dp)