class Solution {
    public int maxJump(int[] stones) {
        
        if(stones.length==2){
            
            return stones[1] - stones[0];
        }
        
        int maxi = 0;
        
        for(int i=2;i<stones.length;i+=2){
            
            maxi = Math.max(maxi, stones[i]-stones[i-2]);
        }
        
        for(int i=1;i<stones.length-2;i+=2){
            
            maxi = Math.max(maxi, stones[i+2]-stones[i]);
        }
        
        return maxi;
        
    }
}