class Solution:
    def climbStairs(self, n: int) -> int:

        x = 1
        y = 0
        
        for i in range(n):
            
            x,y = x+y,x
        #print(x,y)
        return x