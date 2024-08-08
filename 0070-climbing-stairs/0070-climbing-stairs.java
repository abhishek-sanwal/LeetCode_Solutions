class Solution {
    public int climbStairs(int n) {
        
        if(n==1){
            return 1;
        }
        
        int prev = 1, curr = 2;
        
        for(int i=3;i<=n;i++){
            
            int temp = curr;
            curr = prev + curr;
            prev = temp;
            
        }
        
        return curr;
        
//         //  Creation of dp array        
//         int[] dp = new int[Math.max(3,n+1)];
        
//         // Initilization
//         dp[0] = 0;
//         dp[1] = 1;
//         dp[2] = 2;
//         // Bottom-up dp
//         for(int i=3;i<=n;++i)
//                 dp[i] = dp[i-1] + dp[i-2];
//         return dp[n];
        
        
    }
}