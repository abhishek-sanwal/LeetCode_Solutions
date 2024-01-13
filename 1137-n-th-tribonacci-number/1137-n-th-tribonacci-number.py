class Solution:
    def tribonacci(self, n: int) -> int:
        
        # For TopDown DP
        
        # Guard Condition
        
        # Base Condition [Smallest subproblem and its solution]
        
        # Check whether case is memorized or not
        
        # Recurrance relation [How we can break the problem into sub-problems]
        
        # Memorized the recursion call
        
        # Return memorized call
        
        # larger n values => smaller n values
        
        memo = dict()
        def TopDown(n:int)->int:
            '''
            TopDown Dp to calculate nth tribonacci number
            TC => 0(3^N)
            SC => 0(3^n)
            '''
            '''
            TC => 0(N)
            SC => 0(N)
            '''
            # Base Condtion 1
            if n<2:
                
                return n
            
            # Base Conditon 2
            
            if n == 2:
                return 1
            
            # Memorization Case
            if n in memo:
                return memo[n]
            # Recurracne relation
            
            memo[n] = TopDown(n-1) + TopDown(n-2) + TopDown(n-3)
            return memo[n]
        
        # Opposite to TopDown
        # Smaller n values to larger n values
        
        # Initilization of Dp array
        # Guard Conditons
        
        # Recurrance relation logic
        # Can we optimize space [ Space Optimization]
        
        def BottomUp(n:int)->int:
            
            '''
            BottomUp Dp to calculate nth tribonacci number
            TC => 0(N)
            SC => 0(N)
            '''
            
            # Initilization for dp array
            
            dp = [0,1,1] + [0] *(n-2)

            for i in range(3,n+1):
                
                # recurrance relation f(n) = f(n-1) + f(n-2) + f(n-3)
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            
            return dp[n]
        
        def Optimized_BottomUp(n:int)->int:


            # Optimized Space Complexity
            # Sc => 0(N)
            # TC => 0(N)
            
            # Initilization of dp array
            dp = [0,1,1]
            
            # Recurrance loop
            for i in range(3,n+1):

                dp[i%3] = sum(dp)

            return dp[n%3]
            
        
        # Guard Condition
        if n >= 0 and type(n) == int:
            
            #return TopDown(n)
            return Optimized_BottomUp(n)
        
        return -1
            
            
        #Bottom Up Dp 
        
        # Guard Conditons
        # Base Condtions [Solution for smallest subproblems]
        # Initilization of DP []
        # Recurrance relation[ How to fill dp]
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        dp = [-1] * 40
        dp[0] = 0
        dp[1] = dp[2] =1
        
        # Topdown dp
        def topdown(n):
            
            nonlocal dp
            
            if dp[n] != -1:
                
                return dp[n]
            
            dp[n] = topdown(n-1) + topdown(n-2) + topdown(n-3)
            # Tn = Tn-1 + Tn-2 + Tn-3 for n >= 0.
            return dp[n]
        
        # bottomup dp
        def bottomup(n):
            
            nonlocal dp
            
            for i in range(3,n+1):
                
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            
            return dp[n]
        
                
        #bottomup(n)
        #topdown(n)
        #return dp[n]
        
        # No-dp each subproblem depends upon previous three subproblems
        
        if n==0:
            return 0
        
        x,y,z =1,1,0
        
        for i in range(3,n+1):
            x,y,z = x+y+z,x,y
            
        return x
            
        
        