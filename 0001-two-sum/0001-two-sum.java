class Solution {
    public int[] twoSum(int[] nums, int target) {
     
        int res[] = new int[2];
        
        HashMap<Integer,Integer> mapp = new HashMap<Integer, Integer>();
        
        for(int i=0;i<nums.length;++i){
            
            int req = target - nums[i];
            
            if(mapp.containsKey(req)) 
            {
                return new int[] {mapp.get(req),i};
            }
            mapp.put(nums[i],i);
            
        }
    
        return null;
        
           
    }
}