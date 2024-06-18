class Solution {
    public int maxProfitAssignment(
        int[] difficulty,
        int[] profit,
        int[] worker
    ) {
        
        // int maximumAbility = Arrays.stream(worker).max().getAsInt();
        int maximumAbility = IntStream.of(worker).max().getAsInt();
        // System.out.println(maximumAbility);
        int[] ability = new int[maximumAbility+1];
        
        for(int i=0;i<difficulty.length;++i){
            
            if(difficulty[i] <= maximumAbility )
                    ability[difficulty[i]] = Math.max(ability[difficulty[i]], profit[i]);
            
        }
        
        // Create prefix maxima array
        for(int i=1;i<=maximumAbility;++i)
                ability[i] = Math.max(ability[i], ability[i-1]);
        
        int totalProfit = 0;
        for(int currWorker:worker){
            
            totalProfit += ability[currWorker];
            
        }
        return totalProfit;
        
    }
}